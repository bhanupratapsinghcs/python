# Maximum and minimum of an array using minimum number of comparisons
# Tournament Method


def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]

    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        print('first', arr_max, arr_min)
        return (arr_max, arr_min)

    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
            print('second', arr_max, arr_min)
        else:
            arr_max = arr[high]
            arr_min = arr[low]
            print('second', arr_max, arr_min)
        return (arr_max, arr_min)
    else:

        # If there are more than 2 elements
        mid = int((low + high) / 2)
        print(mid)
        print('half')
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        print(3, arr_max1, arr_min1)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)
        print(arr_max2, arr_min2)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

# Cpmapare in pairs
def ComparePair(arr, n):

    if n == 0:
        return(arr[n], arr[n])
    if arr[0] > arr[1]:
        arr_max = arr[0]
        arr_min = arr[1]
        print('yes')
    else:
        arr_max = arr[1]
        arr_min = arr[0]
        print('yes-')

    i = 2 if n % 2 == 0 else 1
    while i < n - 1:
        if arr[i] < arr[i + 1]:
            arr_max = max(arr_max, arr[i + 1])
            arr_min = min(arr_min, arr[i])
            print('yes--')
        else:
            arr_max = max(arr_max, arr[i])
            arr_min = min(arr_min, arr[i + 1])
            print('yes---')
        print('yes----')
        i += 2

    return(arr_max, arr_min)


# Driver code
arr = [1000, 11, 445, 1, 330, 3000, 0, 4000, -1]
high = len(arr) - 1
low = 0
# arr_max, arr_min = getMinMax(low, high, arr)
arr_max, arr_min = ComparePair(arr, len(arr))
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)
