import datetime as dt
from datetime import datetime, timedelta
import time
current_day = dt.datetime.now()
today_date = dt.timedelta()
no_of_days = 30
def get_date(no_of_days):
    day = no_of_days % 2
    if day != 0:
        return (current_day + today_date )
    else:
        return (current_day - today_date)
print(get_date(9))