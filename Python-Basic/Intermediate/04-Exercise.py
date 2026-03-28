from datetime import date, datetime, time

def print_date_value (date):
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(type(date))

my_date = datetime.now()


print_date_value(my_date)


