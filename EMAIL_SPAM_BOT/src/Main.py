import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import the Report.py script for creating statistics file
from Report import generate_report

def establish_smtp_connection(sender_email, app_password):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Log in with your App Password
    server.login(sender_email, app_password)

    return server

def send_email(server, sender_email, recipient_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        return True  # Email sent successfully
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False  # Email send failed

def get_formatted_date_time():
    date_and_time = datetime.now()
    return date_and_time.strftime('%Y-%m-%d %H:%M:%S')

def spam_emails():
    sender_email = 'ondra.losi@gmail.com'  # Insert your sender email
    app_password = 'gsvo ddjz pkoc ujlb'  # Google App password for your account
    subject = 'Spam bot'
    message = 'This email was sent by email-spam-bot script'

    # Prompt for the recipient's email address
    recipient_email = input("Who's email do you want to spam: ")

    # Prompt the user for the number of emails to send
    input_str = input("Enter the number of emails to send: ")
    try:
        num_emails = int(input_str)
    except ValueError:
        print("Please enter a valid number.")
        return

    # Establish the SMTP connection
    server = establish_smtp_connection(sender_email, app_password)

    # Initialize a counter for the number of emails sent
    sent_counter = 0

    # Initialize an empty list to store log messages
    log_messages = []

    start_time = time.time()  # Start the timer here

    for i in range(num_emails):
        sent = send_email(server, sender_email, recipient_email, subject, message)
        sent_counter += 1

        if sent and (sent_counter % 1 == 0 or sent_counter == num_emails):  # Log every 2nd email or the last one
            time_it_took = time.time() - start_time
            time_formatted = "{:.2f}".format(time_it_took)
            date_formatted = get_formatted_date_time()
            status = "OK" if sent else "Failed"
            log_message = f"Email number {sent_counter} | {date_formatted} | Status: {status} | send In: {time_formatted} s"
            log_messages.append(log_message)
            print(log_message)

    # Close the SMTP connection
    server.quit()

    return log_messages  # Return the list of log messages

def save_to_file(log_file, log_messages):
    if log_messages:
        with open(log_file, "a") as file:
            for log_message in log_messages:
                file.write(log_message + "\n")

def main():
    log_file = "src/log.txt"
    log_messages = spam_emails()
    save_to_file(log_file, log_messages)
    print("All e-mails were sent")

    # Statistics
    print("Creating statistics now...")
    report = generate_report(log_file)
    
    # Print the report
    print(report)
    
    # You can also save the report to a text file if needed
    with open("src/statistics.txt", "w") as report_file:
        report_file.write(report)

if __name__ == "__main__":
    # runs function with tests, if some of them fail, the main function wont run!!!!!
    
    # runs the main function 
    main()
