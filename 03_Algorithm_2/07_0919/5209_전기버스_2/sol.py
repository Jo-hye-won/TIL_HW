import sys
sys.stdin = open('input.txt')

# r : 사용한 원소의 개수
# acc : 충전 횟수
# gas : 이동 가능한 거리 -> 유망성 조사의 대상
def search(r, acc, gas):
    global result
    # print(r, acc, gas)
    # 종료시점 -> 내 버스가 종점에 도착한 상황
    if acc >= result:
        return
    if r == N - 1:
        # 여기까지 오시는데 충전 몇번 하셨습니까?
        if acc < result:
            result = acc
    else:
        if gas: # 가스가 있을 때만! 없는데 가면 안돼ㅋㅋㅋㅋ
            # 충전 안한고 다음칸 가기
            search(r+1, acc, gas - 1)
        # 충전 하고 다음칸 가기
        search(r+1, acc+1, arr[r] - 1)


T = int(input())
for tc in range(1, T+1):
    N, *arr = list(map(int, input().split()))
    # print(N, arr)
    result = N # 모든 정류소에서 다 충전 한 상황이 최악의 상황일 것
    search(0, 0, arr[0])
    print(f'#{tc} {result}')