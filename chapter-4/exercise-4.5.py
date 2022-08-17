# Chapter 4 - Exercise 4.6
# practice practice practice!!!

def computepay(hours, rate):
    extratime = (1.5 / rate) * 100 + rate
    pay = hours * rate + extratime
    return pay


hrs = input('Enter hours: ')
exrate = input('Enter rate: ')

hrs = int(hrs)
exrate = float(exrate)

pay = computepay(hrs, exrate)
print('Pay:', pay)
