from datetime import datetime 

def get_current_date():
    print(datetime.now().strftime("%Y-%m-%d"))

def get_diference_date (in_date, ot_date):
    in_date = datetime.strptime(in_date, "%Y-%m-%d")
    ot_date = datetime.strptime(ot_date, "%Y-%m-%d")
    difference = ot_date - in_date
    return print(f"La diferencia es de {difference.days} dias")

