def mergeSort(b):
    if len(b) > 1:
        mid = len(b)//2
        L = b[:mid]
        R = b[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                b[k] = L[i]
                i+= 1
            else:
                b[k] = R[j]
                j+= 1
            k+= 1
        while i < len(L):
            b[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            b[k] = R[j]
            j+= 1
            k+= 1


def printList(b):
    for i in range(len(b)):
        print(b[i], end =" ")
    print()
b = [33, 4, 5, 66]
print(b)
print('result')
mergeSort(b)
printList(b)
