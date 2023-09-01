import sys
sys.stdin = open('input.txt')

# def int_to_string(cards):
    # cards = list(map(str, str(cards)))
    # arr = [0] * N
    # for k in range(N):
    #     arr[2] = cards % 10
    #     cards = cards //10
    #
    #     arr[1] = cards % 10
    #     cards = cards // 10
    #
    #     arr[0] = cards % 10
    #     cards = cards // 10

    # cards = list(str(cards))

def swap(cards, i, j):
    arr = [0] * N
    for k in range(N):
        arr[N-1-k] = str(cards % 10)
        cards = cards // 10

    arr[i], arr[j] = arr[j], arr[i]
    num = int(''.join(arr))
    return num

# cards = 순열 대상
# now = 현재 조사위치
# r = 최대 조사횟수(최대교환횟수)
3
def perm(cards, now, r):
    global result
    # 내가 만들 수 있는 모든 경우의 수에 대해서
    for i in range(720):
        # now번 swap했을 때, i번째 경우의 수에 올 수 있는 수가 아직 기록되지 않았다면
        if memo[now][i] == 0:
            memo[now][i] = cards
            break
        elif memo[r][i] == cards:
            return

    if now == r: # 내 조사회수가 최대조사회수와 동일해졌다.
        if cards > result: # 최대값 갱신
            result = cards
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                # cards[i], cards[j] = cards[j], cards[i]
                cards = swap(cards, i, j)
                perm(cards, now+1, r)


T = int(input())

for tc in range(1, T+1):
    cards, r = list(map(int, input().split()))
    N = len(str(cards))
    # R번째일 때, 만들어질 수 있는 최대 경우의 수를 모두 기록할 수 있는 리스트
    # arr = 123
    # 0번째일때, 만들어질수 있는 경우의 수
    # 1번째일때, 만들어질수 있는 경우의 수
    # index == 0: 한번도 교환안한 경우
    # 최대 교환 횟수가 10
    # 각 횟수차마다 들어갈수 있는 최대 경우의 수
    # 순열의 경우 N에 대한 모든 경우의 수 = N! 최대 N -> 6! = 720
    memo = [[0]*720 for _ in range(11)]
    result = -0
    perm(cards, 0, r) # 배열, 시작점, 끝점
    print(memo)