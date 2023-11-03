def read_log_file(log_file):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []

def calculate_statistics(log_lines):
    total_emails = len(log_lines)
    sent_emails = sum('Status: OK' in line for line in log_lines)
    failed_emails = total_emails - sent_emails
    success_rate = (sent_emails / total_emails) * 100 if total_emails > 0 else 0

    time_data = [line.split(" | ") for line in log_lines if 'Status: OK' in line]
    if time_data:
        times = [float(data[-1].split(":")[-1][:-2]) for data in time_data]
        avg_time = sum(times) / len(times)
        earliest_time_data = min(time_data, key=lambda data: data[1])
        latest_time_data = max(time_data, key=lambda data: data[1])
        earliest_email_number = int(earliest_time_data[0].split(" ")[-1])
        latest_email_number = int(latest_time_data[0].split(" ")[-1])
    else:
        avg_time = 0
        earliest_email_number = "N/A"
        latest_email_number = "N/A"

    return total_emails, sent_emails, failed_emails, success_rate, avg_time, earliest_email_number, latest_email_number

def generate_report(log_file):
    log_lines = read_log_file(log_file)
    total_emails, sent_emails, failed_emails, success_rate, avg_time, earliest_email_number, latest_email_number = calculate_statistics(log_lines)

    report = "----------------------------------\n"
    report += f"Total Emails Sent: {total_emails}\n"
    report += f"Successful Emails: {sent_emails}\n"
    report += f"Failed Emails: {failed_emails}\n"
    report += f"Success Rate: {success_rate:.2f}%\n"
    report += f"Average Time Taken: {avg_time:.2f} seconds\n"
    report += f"Earliest Sent Email: number{earliest_email_number}\n"
    report += f"Latest Sent Email: number {latest_email_number}\n"
    report += "----------------------------------\n"

    return report


