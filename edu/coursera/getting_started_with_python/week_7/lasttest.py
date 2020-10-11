largest = None
smallest = None


while True:
    n = input("Enter number: ")
    if n == "done" : break
    try:
        n=int(n)
        if largest is None or largest < n:
            largest = n
        if smallest is None or smallest > n:
            smallest = n
    except:
        print("Invalid input")
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
