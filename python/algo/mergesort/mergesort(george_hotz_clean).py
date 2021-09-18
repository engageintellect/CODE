
nums = [44,33,2,35,64,36,86,22,1]


def MergeSort(nums):

    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid:]
        right = nums[mid:]

        MergeSort(left)
        MergeSort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k]=right[j]
            j+=1
            k+=1

        print("Merging...", nums)


MergeSort(nums)
print("after:", nums)
