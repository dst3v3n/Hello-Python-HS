### Dates ###

from datetime import datetime



def print_date (date):
    print(date.year)
    print(date.month)
    print(date.day)  
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

now = datetime.now()

print_date(now)

year_2023 = datetime(2023 , 1 , 1, 10 , 42 , 50 ) #Exige almenos 3 argumentos: Fecha, mes y dia

print_date(year_2023)

from datetime import time

current_time = time(21 , 6 , 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2023 , 5 , 11)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year , current_date.month + 1 , current_date.day)

print(current_date.year)
print(current_date.month)
print(current_date.day)

diff = year_2023 - now  #Restarlo
print(diff)

diff = year_2023.date() - current_date #Con el punto especificamos que variable queremos restar
print(diff)

# diff = year_2023.time() - current_time
# print(diff)

from datetime import timedelta #Franjas de fechas

start_timedelta = timedelta(200 , 100 , 100 , weeks= 10)
end_timedelta = timedelta(300 , 100 , 100 , weeks= 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta) 