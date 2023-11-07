import pandas as pd

# Load the Excel file
excel_file_path = "src/Emails/spam_emails.xlsx"  # Update with your Excel file path
df = pd.read_excel(excel_file_path, engine='openpyxl')

# Select the first 100 rows
emails = df['Email']

# Convert the 'emails' column to a list
email_list = emails.tolist()

print("-----------------------")
print(len(email_list))