h1 = input("Enter Hours: ")
r2 = input("Enter Rate: ")


hours = float(h1)
rate = float(r2)


orate = 1.5 * rate


def computepay():
    if hours > 40:
        otime = (hours - 40) * orate
        reg = 40 * rate
        pay = otime+reg

computepay()

print(pay)
