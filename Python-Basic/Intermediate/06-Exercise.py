from datetime import datetime

def transform_to_timestamp(date):
    timestamp = date.timestamp()
    return print(timestamp)


my_date = datetime.now()


transform_to_timestamp(my_date)
