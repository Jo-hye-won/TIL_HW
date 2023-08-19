import sys
sys.stdin = open('view.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())  # 건물의 개수 N
    h = list(map(int, input().split())) # N개의 건물의 높이
    cnt = 0 # 세대의 수 카운트
    for i in range(2, N-1):
        max_h = h[i]  # 가운데를 기준으로 얘가 최대조망권 초기설정값이됨
        for j in range(i-2, i+3):   # 양쪽 2칸씩 비교해야함
            if i == j:  # 나와 나자신을 비교할 필요는 없다
                continue    # 지나가쟈
            if h[i] > h[j] and max_h > h[i]-h[j]:
                # 조사대상이 양 옆두개씩보다 크고,
                # 그 둘의 차이가 최대 조망권보다 작으면
                max_h = h[i]-h[j]
                # 최대 조망권을 그 차이로 변경하기
            elif h[i] <= h[j]:  # 하나라도 더 높은 경우가 잇으면
                # 확보 안되니까 더이상 조사할 필요 없음
                break
        else: # elif로 가서 안멈추고 종료되지 않았으면
                # 정상적으로 잘 조사된 것이니까
                # 조망권 다 더해주기
            cnt += max_h
    print(f'#{tc} {cnt}')

