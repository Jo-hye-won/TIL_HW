N, M = map(int, input().split())
dduck = lis(map(int, input().split()))

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in dduck:
        if x > mid:
            total +=