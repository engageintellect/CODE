def computepay(h, r):
	hours = float(h)
	rate = float(r)
	
	orate = 1.5 * rate
	
	if hours > 40:
	    otime = (hours - 40) * orate
	    reg = 40 * rate
	    return otime + reg
	




hrs = input("Enter Hours: ")
rt = input("Enter Pay: ")

p = computepay(float(hrs),float(rt))

print("Pay", p)



