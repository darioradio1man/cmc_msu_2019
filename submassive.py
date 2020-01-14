from sys import maxsize


def maxsubarraysum(a, size):
    maxfar = -maxsize - 1
    maxend = 0
    s = 0
    for i in range(0, size):
        maxend += a[i]
        if maxfar < maxend:
            maxfar = maxend

        if maxend < 0:
            maxend = 0
            s = i + 1

    print(maxfar)


a = [2, 3, -7, -1, 3, 4, 5, -2, -4, 7, 8, -6, 1]
maxsubarraysum(a, len(a))
