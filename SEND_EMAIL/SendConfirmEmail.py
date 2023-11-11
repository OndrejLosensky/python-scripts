from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirm_email( marked_emails):
    # Date
    date = datetime.now()
    date_formated = date.strftime('%Y-%m-%d %H:%M:%S')    

    sender_email = ''  # Insert your sender email
    app_password = ''  # Google App password for your account

    recipient_email = 'email.address@gmail.com' # Email where you want to send it to

    subject = 'This message was sent via python'
    message = f'you can adjust this by your needs \n for example you can print date {date_formated}' # This will add date to the body of the e-mail

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
        
    # Connect to the Gmail SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Log in with your App Password
    server.login(sender_email, app_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Close the connection
    server.quit()

    print("Confirmation e-mail was sent successfully!")
