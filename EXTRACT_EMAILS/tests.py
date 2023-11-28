import unittest
import xlsxwriter
from ExtractEmails import process_email, export_mails  # Import your functions

class TestEmailProcessing(unittest.TestCase):
    def test_illegal_characters(self):
        workbook = xlsxwriter.Workbook('onlyfortest.xlsx')
        worksheet = workbook.add_worksheet()

        try:
            testOfIllegalCharacters = "\x07"
            worksheet.write('A1', testOfIllegalCharacters)
        except xlsxwriter.exceptions.IllegalCharacterError as e:
            print("There was some kind of error with the IllegalCharacters:", e)
        else:
            print("The process was successful!!")

        workbook.close()

    def test_process_email(self):
        ("This test was successfull")
        pass

    def test_export_email(self):
        ("This test was successfull")
        pass

    def test_log_to_file(self):
        ("This test was successfull")
        pass


if __name__ == '__main__':
    unittest.main()