import time
while True:
    date = input('Date (m/dd/yyyy): ')
    try:
        date = time.strptime(date, '%m/%d/%Y')
        break
    except ValueError:
        print('Invalid date!')
        continue
