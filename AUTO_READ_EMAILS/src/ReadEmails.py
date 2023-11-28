import time
from datetime import datetime
import yaml
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Report import generate_report
from NameOfTheDay import get_current_day

# confirmation to email address
def send_confirm_email( marked_emails):
    # Function to send confirmation e-mail after SUCCESSFULLY reading emails
    # In the Main function we can create and IF statement for if the mark_as_seen() wasnt successfull and also send email

    # simple function to create variable for date
    date = datetime.now()
    date_formated = date.strftime('%Y-%m-%d %H:%M:%S')    

    sender_email = ''  # Insert your sender email
    app_password = ''  # Google App password for your account

    recipient_email = 'l' # Email where you want to send it to

    subject = 'Script for auto-reading e-mails'
    message = f'Script ran successfully \n time it took:{time}. \n Number of marked e-mails as seen: {marked_emails} \n Todays date: {date_formated} '
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

    print("E-mail was sent successfully")



def mark_as_seen(login_file):
    # Function that logs into the email Inbox and then simply marks them all as SEEN
    log_file = "src/log/log.txt"
    
    # Reads data from the login file | "login.yaml"
    with open(login_file) as f:
        content = f.read()

    # loads up the data from it
    my_credentials = yaml.load(content, Loader=yaml.FullLoader)
    print("Loggining to: ", my_credentials["user"])
    start_time = time.time()
    time.sleep(1)

    # your credentials to inicialize the login
    user, password = my_credentials["user"], my_credentials["password"]

    # IMAP for Gmail
    imap_url = 'imap.gmail.com'

    # Logs into the gmail
    my_email = imaplib.IMAP4_SSL(imap_url)
    my_email.login(user, password)
    my_email.select('Inbox')
    print("I have opened your Inbox")

    _, data = my_email.search(None, 'ALL')  # Searches all the emails

    # List of all email ID's
    list_emails = data[0].split()

    # Number of all emails in your Inbox
    num_emails = len(list_emails)

    # Prints out the number
    print("Number of all emails:", num_emails)
    print("--------------------------------------")

     # Vyhledá nepřečtené emaily
    _, data = my_email.search(None, 'UNSEEN')
    unseen_email_ids = data[0].split()

    # Počet nepřečtených e-mailů
    global  num_unseen_emails
    num_unseen_emails = len(unseen_email_ids)

    if num_unseen_emails > 0:
        print("Number of unseen e-mails:", num_unseen_emails)
        print("--------------------------------------")

        for email_id in unseen_email_ids:
            my_email.store(email_id, '+FLAGS', '\Seen')

        print("I have marked all e-mails as SEEN")
        global time_in_seconds
        time_in_seconds = time.time() - start_time

        current_day = get_current_day()
        log_message = f"{num_unseen_emails} e-mails marked as seen | account: {user}  | Time it took: {time_in_seconds:.2f}s | day: {current_day}"
        log_to_file(log_message, log_file)
        global successfull 
        successfull = True
    else:
        successfull = False


    # Logs out of your email
    my_email.logout()

    return num_unseen_emails

def log_to_file(log_message, log_file):
    #timestamp = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{log_message}"
    #separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        #f.write(separator + "\n")
        f.write(log_entry + "\n")
        #f.write(separator + "\n")
    
    print("Log was saved successfully!")


def main():
    print("----------------------------------")
    print("Initializing to read e-mails...")
    time.sleep(1)

    # FUNCTION TO MARK ALL EMAILS AS SEEN   
    login_file = "src/login.yaml"
    num_unseen_emails = mark_as_seen(login_file)  # Call mark_as_seen and get the values

    # FUNCTION TO SEND CONFIRMATION EMAIL TO MY ADDRESS

    if successfull == True:
        send_confirm_email(num_unseen_emails)

        print("Creating statistics now...")
        log_txt = "src/log/log.txt"
        report = generate_report(log_txt)
        
        # Print the report
        print(report)

        # This saves the values to text file || It could also possibly generate .html report for better looks
        with open("src/Statistics/statistics.txt", "w") as report_file:
            report_file.write(report)
        print("Done!")

    elif successfull == False:
        print("Your e-mail address didnt have any unred e-mails or something went WRONG!")

if __name__ == "__main__":
    main()