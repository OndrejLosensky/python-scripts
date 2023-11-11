import datetime

def get_current_day():
    global now
    now = datetime.datetime.now()
    
    day_of_week = now.weekday()

    # List of days in a week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    return days[day_of_week]


def main():
    current_day = get_current_day()
    current_date = now.strftime("%d")
    # This tells what the suffix will be after the number
    global suffix
    if current_date == 1:
        suffix = "st"
    elif current_date == 2:
        suffix = "nd"
    elif current_date == 3:
        suffix = "rd"
    else:
        suffix = "th"

    get_date_plus_day = (current_day + " " + current_date + suffix)
    print(get_date_plus_day)


if __name__== "__main__":
    main()


# This is super simple, but can be useful
# I am using this in my other script which is much bigger
