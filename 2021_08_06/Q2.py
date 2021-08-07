import datetime as dt
import time as tm
def get_datetime(num_of_days):
    if (num_of_days % 2) == 0:
        return dt.datetime.today() + dt.timedelta(no_days=num_of_days)
    elif (num_of_days % 3) == 0:
        return dt.datetime.today() - dt.timedelta(no_days=num_of_days)
    else:
        return dt.datetime.today()


