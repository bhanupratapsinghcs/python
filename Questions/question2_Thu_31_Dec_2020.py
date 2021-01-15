class minmax(object):

    def __init__(self):
        self.mn = 0
        self.mx = 0


def getmnmx(arr, n):
    mnmx = minmax()
    if len(arr) == 1:
        mnmx.mn = arr[0]
        mnmx.mx = arr[0]
        return mnmx
    if arr[0] > arr[1]:
        mnmx.mn = arr[1]
        mnmx.mx = arr[0]
    else:
        mnmx.mn = arr[0]
        mnmx.mx = arr[1]
    for x in range(2, n):
        if arr[x] > mnmx.mx:
            mnmx.mx = arr[x]
        elif arr[x] < mnmx.mn:
            mnmx.mn = arr[x]

    return mnmx


if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    n = 6
    r = getmnmx(arr, n)
    print(r.mn, r.mx)
