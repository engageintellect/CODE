# BINARY SEARCH

def searchList(needle, haystack):
    lo = 0
    hi = len(haystack) - 1

    while lo <= hi:
        m = lo + (hi - lo) // 2
        v = haystack[m]

        if v == needle:
            print(f'{needle} is in haystack')
            return True

        elif v > needle:
            hi = m - 1
        else:
            lo = m + 1

    print(f'{needle} is not haystack')
    return False


haystack = [2, 2, 8, 8, 9, 10, 11, 39, 44, 44, 72, 91]  # Sorted
needle = 8
print(searchList(needle, haystack))

