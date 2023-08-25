import sys
sys.stdin = open('input.txt')

'''
겹치는 만큼 기다려야하니까 가장 많이 겹치는 만큼이 최소 걸리는 시간이 되겠다!!
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 학생 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    # for _ in range(N):
    #     go, to = map(int, input().split()) # 현재 방과 돌아갈 방
    #     print(go,to)
    # print(arr)

    cnt = [0] * 201         # 방사이 공간을 지나는 사람수를 기록할 복도
    for a, b in arr:        # arr에서 두개 꺼낼건데 a <= b라는 보장이 없음에 주의!!
                            # 복도번호 = (방번호 + 방번호%2) // 2
        a = (a + a % 2)//2
        b = (b + b % 2)//2
        for i in range(min(a, b), max(a, b)+1):  # 둘 중 작은데서 출발해서 둘중 큰곳으로 도착
            cnt[i] += 1
    print(f'#{tc} {max(cnt)}')
