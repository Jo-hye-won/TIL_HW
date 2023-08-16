import sys
sys.stdin = open('input.txt')

def search(now, acc):
    global result
    # 가지치기는 똑같이 진행
    # 내 누적값이 최종 결과값보다 한번이라도 커지만, 더이상 조사 x
    if acc > result:  # 음수가 있을 경우에는 이 가지치기 안해도 됨
        return
    # 언제까지 조사 할거냐? => now가 N이 되면 모든 열에 대한 탐색 끝
    if now == N:
        if acc < result:
            result = acc
    else:
        # 현재 열(now)에서 가능한 모든 행(row)를 탐색
        for row in range(N):
            # 아직 방문한 적 없다면, 쓸거임
            if visited[row] == 0:
                visited[row] = 1
                search(now + 1, acc + arr[now][row])
                visited[row] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 10 * N      # 최솟값 초기화
    visited = [0] * N    # 행의 방문 여부를 저장하는 리스트

    # 시작점, 누적값
    search(0, 0)

    print(f'#{tc} {result}')