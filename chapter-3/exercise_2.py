# rate is 10

hours = input('Enter hours: ')
rate = input('Enter rate: ')
#pay = int(hrs) * float(rate)

overtime = 1.5  # time and a half  overtime

try:

    hrs = int(hours)
    rate = float(rate)
    overtime = (1.5 / rate) * 100

    # calculate rate at 1.5 times
    # give 1.5 times the hourly rate above 40 hours
    hourlyRate = ''
    rateAboveFortyHours = overtime + rate

    if hrs > 40:
        hourlyRate = hrs * rate + rateAboveFortyHours
    else:
        hourlyRate = hrs * rate

    print('Pay:', hourlyRate)

except:
    print('Error, please enter numeric input.')
