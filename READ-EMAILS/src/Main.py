import time
from datetime import datetime
import yaml
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_confirm_email(time, marked_emails):
    # Function to send confirmation e-mail after SUCCESSFULLY reading emails
    # In the Main function we can create and IF statement for if the mark_as_seen() wasnt successfull and also send email
    # simple function to create variable for date
    date = datetime.now()
    date_formated = date.strftime('%Y-%m-%d %H:%M:%S')    


    sender_email = '' # Insert the email you send it from
    app_password = '' # Google App password for your account
    recipient_email = '' # Email where you want to send it to

    subject = 'Your script was successfull'
    message = f'Time it took:{time}. \n Number of marked emails: {marked_emails} \n Date and time: {date_formated}'
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


def process_email():
    email_id = ""
    email_data = {
        "ID": email_id,
    }



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

    # Logs into the gmaik
    my_email = imaplib.IMAP4_SSL(imap_url)
    my_email.login(user, password)
    my_email.select('Inbox')
    print("I've opened your Inbox")

    _, data = my_email.search(None, 'ALL')  # Searches all the emails

    # List of all email ID's
    list_emails = data[0].split()

    # Number of all emails in your Inbox
    num_emails = len(list_emails)

    # Prints out the number
    print("Number of all your emails:", num_emails)
    print("--------------------------------------")

    global number_of_marked_emails
    number_of_marked_emails = 50 # Change to your desired number

    # marks last X emails as SEEN, you can adjust it by changing the variable
    start_index = max(0, num_emails - number_of_marked_emails)
    for email_id in list_emails[start_index:]:
        my_email.store(email_id, '+FLAGS', '\Seen')

    print("I've marked last", number_of_marked_emails, "emails as SEEN")
    timeInSecond = (time.time() - start_time)
    global Time_It_Took
    Time_It_Took = "{:.2f}".format(timeInSecond) # Formated time to only have two decimals behind the ','

    # writes log message to the log.txt
    log_message = f"Marked {number_of_marked_emails} as SEEN on the {user}  |  In time: {Time_It_Took}s"
    log_to_file(log_message, log_file)

    # Logs out of your email
    my_email.logout()

    # sets this variable to true when running this so i can now execute the confirmation email send
    global successIsTrue
    successIsTrue = True
def log_to_file(log_message, log_file):
    timestamp = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{timestamp}   {log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")
    
    print("log was saved successfully!!")


def main():
    print("----------------------------------")
    print("Initializing to read the e-mails...")
    time.sleep(1)

    # FUNCTION TO MARK ALL EMAILS AS SEEN   
    login_file = "src/login.yaml"
    mark_as_seen(login_file)

    if successIsTrue == True:
        # FUNCTION TO SEND CONFIRMATION EMAIL TO MY ADDRESS
        timeStart = Time_It_Took + "s"
        marked_emails = number_of_marked_emails
        send_confirm_email(timeStart, marked_emails)
        print("Email sent successfully!")
    
    elif successIsTrue != True:
        print("Something went wrong... please try that again")

    

if __name__ == "__main__":
    main()