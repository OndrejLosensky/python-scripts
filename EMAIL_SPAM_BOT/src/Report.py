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

    # Create a dictionary to store unique timestamps and their corresponding times
    time_data = {}
    email_times = {}  # Store email times to find fastest and slowest
    total_time = 0

    for line in log_lines:
        if 'Status: OK' in line:
            parts = line.split(" | ")
            if len(parts) >= 4:
                timestamp = parts[3]  # Extract the timestamp
                email = parts[0]  # Extract the email address
                time_str = parts[2].split(":")[-1][:-2]  # Extract the time in seconds
                try:
                    time_float = float(time_str)
                    if timestamp not in time_data:
                        time_data[timestamp] = []
                    time_data[timestamp].append(time_float)
                    total_time += time_float

                    # Track email times
                    if email not in email_times:
                        email_times[email] = []
                    email_times[email].append(time_float)
                except (ValueError, IndexError):
                    # Handle invalid or empty time values
                    pass

    avg_times = []

    for times in time_data.values():
        if times:
            avg_time = sum(times) / len(times)
            avg_times.append(avg_time)

    avg_time = sum(avg_times) / len(avg_times) if avg_times else 0

    # Find the fastest and slowest emails
    fastest_email = max(email_times, key=lambda email: max(email_times[email]))
    slowest_email = max(email_times, key=lambda email: min(email_times[email]))

    return total_emails, sent_emails, failed_emails, success_rate, avg_time, fastest_email, slowest_email, total_time

def generate_report(log_file):
    log_lines = read_log_file(log_file)
    total_emails, sent_emails, failed_emails, success_rate, avg_time, fastest_email, slowest_email, total_time = calculate_statistics(log_lines)

    report = "----------------------------------\n"
    report += f"Total Emails Sent: {total_emails}\n"
    report += f"Successful Emails: {sent_emails}\n"
    report += f"Failed Emails: {failed_emails}\n"
    report += f"Success Rate: {success_rate:.2f}%\n"
    report += f"Average Time Taken: {avg_time:.2f} seconds\n"
    report += f"Fastest Email Sent: {fastest_email}\n"
    report += f"Slowest Email Sent: {slowest_email}\n"
    report += f"Total Time Taken: {total_time:.2f} min\n"
    report += "----------------------------------\n"

    return report


