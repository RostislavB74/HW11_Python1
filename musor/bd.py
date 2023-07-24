import datetime
#import telebot
#from time import strftime
test_date = input("Ввведите дату в формате 'dd-mm-yyyy': ")
now = datetime.datetime.now()
then = datetime.datetime.strptime(test_date, "%d-%m-%Y")
delta1 = datetime.datetime(now.year, then.month, then.day)
delta2 = datetime.datetime(now.year+1, then.month, then.day)

result = ((delta1 if delta1 > now else delta2) - now).days
print(f'До вашего следущего дня рождения осталось {result} дней')