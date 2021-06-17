# rate is 10

hours = input('Enter hours: ')
rate = input('Enter rate: ')
#pay = int(hrs) * float(rate)

hrs = int(hours)
rate = float(rate)

# calculate rate at 1.5 times
# give 1.5 times the hourly rate above 40 hours
hourlyRate = ''
rateAboveFortyHours = (1.5 / rate) * 100 + rate

if hrs > 40:
    hourlyRate = hrs * rate + rateAboveFortyHours
else:
    hourlyRate = hrs * rate


print('Pay:', hourlyRate)
