# create a computation function that takes 2 args
# input hours, rate with
# time and a half for overtime

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")


def computepay(hours, rate):
    # standard hours = 40
    # overtime = above 40 hours
    # hours(40) * rate(10) + 5=(days) * (1.5 * 10) ???

    hours = float(hours)
    rate = float(rate)

    if hours > 40:
        # pay = hours * rate + (hours - 40) * rate * 1.5  # pay = 525
        #pay = hours * rate + (hours - 40) * rate * 0.5
        #pay = (hours * rate) + rate + 15
        pay = (hours * rate) + (hours - 40) * rate * 0.5
        print("Pay", pay)
    else:
        pay = 40 * 10
        print("Pay", pay)


computepay(hrs, rate)
