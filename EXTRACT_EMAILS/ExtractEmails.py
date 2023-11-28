import imaplib
import email
import time
import xlsxwriter  # Import xlsxwriter library
import re
import random
import yaml

# Function to log some data to .txt file | just informative
def log_to_file(log_message, log_file):
    # shows time in the log.txt
    timestamp = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{timestamp}   {log_message}"
    separator = '-' * len(log_entry)

    with open(log_file, 'a') as f:
        f.write(separator + "\n")
        f.write(log_entry + "\n")
        f.write(separator + "\n")

    print("Process was successful!!")

# Function to possibly shorten the body of email | not using it at the moment
def shortened_body(content_of_message):
    words = re.findall(r'\b\w+\b', content_of_message)
    if words:
        return ' '.join(words[:10])
    return content_of_message

# this function decodes to UTF-8 to display some of the special characters etc.
def decode_payload(payload, charset):
    try:
        return payload.decode(charset)
    except:
        return payload.decode("utf-8", errors="ignore")

NumberOfEmail = 0
# Primary function for processing the emails
def process_email(my_message, email_id, worksheet):
    number_of_attachments = 0  # Variable for counting the attachments
    global NumberOfEmail

    # Increment NumberOfEmail
    NumberOfEmail += 1

    email_data = {
        "ID": email_id,
        "Number": NumberOfEmail,
        "Date": my_message['date'],
        "From": my_message['from'],
        "Subject": my_message['subject'],
        "To": my_message['to'],
        "Body": ""
    }

    for part in my_message.walk():
        content_type = part.get_content_type()
        charset = part.get_content_charset()

        # this formats the text | Subject, from, to, date, body
        if content_type == "text/plain":
            payload = part.get_payload(decode=True)
            decoded_payload = decode_payload(payload, charset)
            email_data["Body"] += decoded_payload  # Append to the email body

    # Replace newline characters and extra spaces with a single space
    email_data["Body"] = ' '.join(email_data["Body"].split())

    # Append the email data to the worksheet
    worksheet.write_row(NumberOfEmail, 0, [
        email_data["ID"],
        email_data["Number"],
        email_data["Date"],
        email_data["From"],
        email_data["Subject"],
        email_data["To"],
        email_data["Body"]
    ])

    return number_of_attachments

# Function for exporting emails to log.txt or the Excel table
def export_mails(login_file, worksheet):
    log_file = "log.txt"
    # Loads your credentials from .yaml file | you will specify the file in the main function
    with open(login_file) as f:
        obsah = f.read()

    # Creates variable to store your credentials
    my_credentials = yaml.load(obsah, Loader=yaml.FullLoader)
    print("Logging to:", my_credentials["user"])
    time.sleep(1)

    # Variable for login
    user, password = my_credentials["user"], my_credentials["password"]
    print("Done!")

    # IMAP for Gmail
    imap_url = 'imap.gmail.com'

    # logins into your Gmail account
    my_email = imaplib.IMAP4_SSL(imap_url)
    my_email.login(user, password)
    my_email.select('Inbox')
    print("I've opened your Inbox!")

    start_time = time.time() # runs the timer for measuring the time it has taken
    _, data = my_email.search(None, 'ALL')  # Searches all emails in the specified folder (inbox)

    # List of all your emails
    list_ids = data[0].split()
    messages = []

    print("Number of all your emails: ", len(list_ids))
    time.sleep(3)

    # prints out information when it starts exporting
    print("------------------")
    print("Extracting emails")
    print("------------------")
    print("Started to proccess all e-mails| status:OK")
    Number_of_emails = 0

    batch_size = 100
    email_batches = [list_ids[i:i + batch_size] for i in range(0, len(list_ids), batch_size)]
    for batch_num, batch_ids in enumerate(email_batches, 1):
        messages = []  # Reset the list of emails for each batch
        Number_of_emails = 0  # Reset the email count for each batch

        # FETCH emails for the current batch
        for number in batch_ids:
            typ, data = my_email.fetch(number, '(RFC822)')
            messages.append(email.message_from_bytes(data[0][1]))
            Number_of_emails += 1

        everything_is_ok = ""

        # If something would go wrong, it would be displayed next to the Batch number
        try:
            if everything_is_ok:
                raise Exception("Everything is OK")

        except Exception as e:
            print(f"Batch {batch_num}: processed {batch_num * 100} emails | status: ERROR - {str(e)}")
        else:
            print(f"Batch {batch_num}: processed {batch_num * 100} emails | status: OK")

        # Process and save emails in this batch
        for my_message in messages:
            email_id = random.randint(10000000, 99999999) # Random number with 8 digits for randomized email ID
            process_email(my_message, email_id, worksheet)

    # prints this when the exporting is done
    print("Loaded!")

    timeInSecond = (time.time() - start_time)
    timeInMinutes = timeInSecond / 60
    timeInMinutesTwoDecimals = "{:.2f}".format(timeInMinutes)

    # Saves data to a folder you specify, and also the name of the file
    workbook.close()
    # Prints out the file path
    print("Data saved to ./all_emails.xlsx")

    # Prints the time it took, the number of emails, the account it was exported from
    print("Process took:", timeInMinutesTwoDecimals, "min", " | ", "Number of emails:", len(list_ids),
          " Account:", {my_credentials['user']})

    # Logs this to "log.txt"
    log_message = f"Account: {user}  Process took: {timeInMinutesTwoDecimals} min   Number of emails: {len(list_ids)} Number of batches = {batch_num}"
    log_to_file(log_message, log_file)

# Main function to call everything
def main():

    global workbook
    print("----------------------------")
    print("Getting ready to export emails...")
    time.sleep(2)
    login = "login.yaml"
    workbook = xlsxwriter.Workbook("Excel_folder/all_emails.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, ["ID", "Number", "Date", "From", "Subject", "To", "Body"]) # This adds a header row to the Excel table
    export_mails(login, worksheet)  # Pass worksheet as an argument
    print("SCRIPT PROCESS FINISHED!")
    time.sleep(3)
    exit()

   

# CALLS THE MAIN FUNCTION
if __name__ == "__main__":
    main()
