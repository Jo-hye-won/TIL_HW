import sys
sys.stdin = open('input.txt')

def make_candidates(visited, now,c): # 방문기록, 현재위치, 후보군 기록할 c
    in_perm = [False] * NMAX
    for i in range(1, now) : # 현재 위치까지
        in_perm[visited[i]] = True   #  visited는 내가 몇번째 행에서 사용했는지 적어둘것
    ncands = 0
    for i in range(1, N+1):
        if in_perm[i] == False:  # 안썻ㅆ을떄
            c[ncands] = i
            ncands += 1
    return ncands



def backtracking(visited, now, end, acc):
    global result
    # 가지치기 (더 이상 유망성 없으니 조사하러 갈 이유가 없다)
    if acc > result:
        return

    c = [0] * MAXCANDIDATES

    # 아직 누적값이 result보다 크지 않아서, 최소값이 될 가능성이 남아잇다면,
    # 언제까지 조사할거니?
    if now == end:  # 그래야 모든 열에 대해 조사가 가능하니까
            # 그래서 지금까지 쌓인 acc가 result보다 작아서
            # 최소값을 갱신할 수 있는지 확인
        if acc < result:
            result = acc
    else:       # 아직 끝나지 않았으면
        now += 1  # 다음위치 조사하러 가도록 해줌
        # 현재 위치의 후보 생성
        ncands = make_candidates(visited, now, c)   # 후보군 생성하고, 그 후보군의 길이를 반환
        for i in range(ncands):
            visited[now] = c[i]
            backtracking(visited, now, end, acc+ arr[now -1][visited[now]-1])
            visited[now] = False  # 다른 후보군 선택하기 위한 선택해제


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최종 결과값  # 각 행, 열에서 값 하나씩 구해서더한 값중 최소값
    result = 10 * N   # 지금 문제의 조건이 10보다 작은 숫자들이니까
                      # 다 10이 들어있다고 생각했을 때가 가장 클 것이고
                      # 이값보다는 작겠지

    # 배열에 드러있는 애들 다 더한것 보다는 작겠지 하고 이렇게 해도 됨
    # for i in range(N):
    #     for j in range(N):
    #         result += arr[i][j]

    # result = sum(sum(arr, []))  # 이케 다 더해도 됨


    MAXCANDIDATES = N  # 최대 후보군 수
    NMAX = N+1
    visited =[False] * NMAX
    # 방문표시, 시작점, 끝점, 누적값
    backtracking(visited, 0, N, 0)

    print(f'#{tc} {result}')