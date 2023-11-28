import datetime

def get_current_day():
    now = datetime.datetime.now()
    day_of_week = now.weekday()
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    return days[day_of_week]

current_day = get_current_day()

