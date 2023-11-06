T = int(input())    # 테스트케이스 개수

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))    # 각각을 정수형으로 변환해서 리스트로 저장
    max_val = arr[0]    # 제일 앞에 있는 값으로 초기화
    min_val = arr[0]    # 1000000(가장 큰값)으로 초기화해도 된다
    for i in range(1, N):
        if max_val < arr[i]:
            max_val = arr[i]
        if min_val > arr[i]:
            min_val = arr[i]
    ans = max_val - min_val
    print(f'#{tc} {ans}')
