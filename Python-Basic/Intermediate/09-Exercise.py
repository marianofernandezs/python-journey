from datetime import date, datetime

date_one = date(2025, 1 ,13)

date_two = date(2025, 5, 14)


if date_one > date_two:
    print(f"La fecha mayor es {date_one}")
elif date_one == date_two:
    print("Ambas fechas son iguales")
else:
    print(f"La fecha mayor es {date_two}")
