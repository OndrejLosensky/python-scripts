import time
from datetime import datetime
from collections import defaultdict

def read_log_file(log_file):
    try:
        with open(log_file, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return []


def calculate_statistics(log_lines):
    num_unseen_emails = 0
    total_time_taken = 0
    days_count = defaultdict(int)

    for line in log_lines:
        if "e-mails marked as seen" in line:
            num_unseen_emails += int(line.split()[0]) if line.split()[0].isdigit() else 0

            time_parts = line.split()
            time_index = time_parts.index('Time') + 2 
            time_value = time_parts[time_index][:-1] if time_index < len(time_parts) else None

            if time_value and time_value.replace('.', '').isdigit():
                total_time_taken += float(time_value)
            else:
                print(f"Warning: I could'nt proccess this line {line}")

            day_index = time_parts.index('days:') + 1
            day = time_parts[day_index]
            days_count[day] += int(line.split()[0]) if line.split()[0].isdigit() else 0

    # Find the day with the maximum total count
    max_day, max_count = max(days_count.items(), key=lambda x: x[1])

    # Find the day with the minimum total count
    min_day, min_count = min(days_count.items(), key=lambda x: x[1])

    average_time_taken = total_time_taken / num_unseen_emails if num_unseen_emails > 0 else 0

    return num_unseen_emails, total_time_taken, average_time_taken, max_day, max_count, min_day, min_count


def generate_report(log_file):
    log_lines = read_log_file(log_file)
    num_unseen_emails, total_time_taken, average_time_taken, max_day, max_count, min_day, min_count = calculate_statistics(log_lines)

    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = time.strftime("%H:%M:%S", time.localtime())

    num_of_lines = len(log_lines)
    emails_per_day = num_unseen_emails / num_of_lines

    report = f"----------- STATISTICS FROM: {current_date} ------------\n"
    report += f"All time e-mails seen: {num_unseen_emails}\n"
    report += f"Duration: {total_time_taken:.2f} s\n"
    report += f"Average time taken for email: {average_time_taken:.2f} s\n"
    report += f"Script ran {num_of_lines} times\n"
    report += f"Average e-mails by day {emails_per_day} \n"
    report += f"Day with most emails {max_day} (count: {max_count}) \n"
    report += f"Day with least emails {min_day} (count: {min_count}) \n"
    report += "----------------------------------------------------------\n"
    report += f"Time when creating this report: {current_time} \n"
    report += "----------------------------------------------------------\n"

    return report