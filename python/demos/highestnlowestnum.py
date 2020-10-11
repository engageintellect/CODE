
nums = []

while True:
    inum = input("Input a number:  ")
    if inum == "done": break
    else:
        nums.append(inum)
    

print("Your numbers are:", nums)


h_num = nums[0]
l_num = nums[1]

for n in nums:
    if n > h_num:
        h_num = n
print("Highest Number:", h_num)


for n in nums:
    if n < l_num:
        l_num = n
print("Lowest Number:", l_num)

print("\n")


