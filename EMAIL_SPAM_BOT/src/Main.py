from Report import generate_report
from SendEmails import main

def main():
    # --------- CALLS FUNCTION WITH TESTS FIRST ------------------------
    # ------------------------------------------------------------------
    # ------------ THIS GENERATES THE STATISTICS -----------------------
    # file with the log
    log_file = "src/log.txt"
    # Statistics
    print("Creating statistics now...")
    report = generate_report(log_file)
    
    # Print the report
    print(report)
    # You can also save the report to a text file if needed
    with open("src/Stats/statistics.txt", "w") as report_file:
        report_file.write(report)
    # ------------------------------------------------------------------

    # ---- THIS CALL THE SEND EMAILS FUNCTION WITH EVERYTHING ----------
    #main()
    # ------------------------------------------------------------------

main()