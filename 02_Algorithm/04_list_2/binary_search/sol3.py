import sys
sys.stdin = open('input.txt')
def binarySearch(N, key):
    s = 1
    cnt = 0
    while s <= N:
        mid = (s + N) // 2
        if mid == key:
           return cnt
        elif mid > key:
            N = mid
            cnt += 1
        else:
            s = mid
            cnt += 1
    return False