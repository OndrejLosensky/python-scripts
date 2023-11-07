import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

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

def spam_emails(sender_email, app_password, subject, message, total_emails, num_emails_per_batch, batch_pause_seconds):
    # Read recipient emails from an Excel file
    recipient_emails = pd.read_excel('src/Emails/spam_emails.xlsx')['Email'].tolist()

    # Establish the SMTP connection
    server = establish_smtp_connection(sender_email, app_password)

    # Initialize an empty list to store log messages
    log_messages = []

    num_batches = total_emails // num_emails_per_batch

    for _ in range(num_batches):
        for recipient_email in recipient_emails:
            for i in range(num_emails_per_batch // len(recipient_emails)):
                start_time = time.time()
                sent = send_email(server, sender_email, recipient_email, subject, message)
                end_time = time.time()
                time_it_took = end_time - start_time
                date_formatted = get_formatted_date_time()
                status = "OK" if sent else "Failed"
                log_message = f"To: {recipient_email} | Status: {status} | send In: {time_it_took:.2f} s | {date_formatted}"
                log_messages.append(log_message)
                print(log_message)
            time.sleep(batch_pause_seconds)

    # Close the SMTP connection
    server.quit()

    return log_messages

def save_to_file(log_file, log_messages):
    if log_messages:
        with open(log_file, "a") as file:
            for log_message in log_messages:
                file.write(log_message + "\n")

def main():
    sender_email = 'email.ads.ondrej@gmail.com'  # Insert your sender email
    app_password = 'rhrp ogho cthw iqig'  # Google App password for your account
    subject = 'Email marketing test'
    message = 'This email was sent by email-spam-bot script'
    total_emails = 40
    num_emails_per_batch = 20  # Change the number of emails to send in each batch
    batch_pause_seconds = 10  # Change the pause duration between batches (e.g., 5 minutes)

    log_file = "src/log.txt"
    log_messages = spam_emails(sender_email, app_password, subject, message, total_emails ,num_emails_per_batch, batch_pause_seconds)
    save_to_file(log_file, log_messages)
    print("All e-mails were sent")

if __name__ == "__main__":
    main()
