import sys
sys.stdin = open('input.txt')

# x, y : 각 좌표값
# acc : 누적값
def DFS(x, y, acc):
    global result # 조사하다가 result보다 큰 누적값이 되어버리면 조사 종료할거라서
    if acc >= result:
        return
    # result의 값을 갱신
    # x, y가 N-1, N-1이 되었을 때 : 맨 오른쪽 아래
    if x == N-1 and y == N-1:
        # result의 값을 갱신
        result = min(acc, result) # 도착했을때
    else:
        # 오른쪽으로 가거나 : y+1 (벽 체크해야함)
        if y + 1 < N:
            DFS(x, y+1, acc + arr[x][y+1])

        # 아래로 가거나
        if x +1 < N:
            DFS(x+1, y, acc + arr[x+1][y])



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 충분히 큰 값
    result = sum(sum(arr, [])) # 내가 받은 이차원 리스트안의 리스트 더하기 리스트 해서 각각의 리스트 안에 있던 정수들모아두고 그 모든 값을 더하기
    # 0, 0 위치에 있는 값으로 시작
    acc = arr[0][0]
    DFS(0, 0, acc)
    print(f'#{tc} {result}')