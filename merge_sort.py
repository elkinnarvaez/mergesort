from sys import stdin

# Declaring this auxiliar array with a fixed size avoids to reserve memory each time that the merge function is called. However, the implementation would also work if this array is created dinamically inside of the merge function.
# MAX represents the maximum number of elements that are going to be ordered and can be set to a high value since it has to be done just once.
MAX = 1000000
AUX = [None for _ in range(MAX)]


def mergesort(A, low, hi):
    assert 0 <= low <= hi <= len(A)
    if low + 1 < hi:
        mid = low + ((hi-low) >> 1)  # mid = (low + hi) // 2
        mergesort(A, low, mid)
        mergesort(A, mid, hi)
        merge(A, low, mid, hi)


def merge(A, low, mid, hi):
    for i in range(low, hi):
        AUX[i] = A[i]
    i, l, r = low, low, mid
    while i != hi:
        if l == mid:
            A[i], r = AUX[r], r+1
        elif r == hi:
            A[i], l = AUX[l], l+1
        else:
            if AUX[l] <= AUX[r]:
                A[i], l = AUX[l], l+1
            else:
                A[i], r = AUX[r], r+1
        i += 1


def main():
    A = [14, 13, 27, 10, 35, 19, 42, 44]
    N = len(A)
    print(A)
    mergesort(A, 0, N)
    print(A)


if __name__ == '__main__':
    main()
