import datetime as dt
from datetime import timedelta
def get_datetime(number_of_days): # function made
    current_date = dt.date.today() # initiliaze current date
    if number_of_days % 2 == 0: # We check number is divisible by 2
        return (timedelta(number_of_days) + current_date)
    elif number_of_days %  3 == 0: # We check number is divisible by 3
        return (timedelta(number_of_days) - current_date)
    else:
        return current_date



