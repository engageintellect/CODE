h1 = input("Enter Hours:")
r1 = input("Enter Rate:")

hours = float(h1)
rate = float(r1)

orate = 1.5 * rate

if hours > 40:
    otime = (hours - 40) * orate
    reg = 40 * rate
    print(otime+reg)
else:
    print(hours * rate)




    







