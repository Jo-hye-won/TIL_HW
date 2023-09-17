## N-Queen

def check(x):
    for i in range(x):
        if row[x] == row[i]:
            return False
        if abs(row[x]-row[i]) == x -i:
            return False
    return True

def dfs(x):
    global result
    if x == n:   # 놓아야 하는 퀸의 개수가 행의 개수와 같으면
                  # 모든 행을 돌아서 한가지 경우가 나온거니까
        result += 1
        print(row)
        print(result)
    else:
        for i in range(n):  # 퀸이 놓이면 다음 칸들은 조사할 필요가 없음
            row[x] = i

            if check(x):
                dfs(x+1)


n = 8  # 놓아야 하는 퀸의 개수
row = [0] * n  # 퀸의 개수만큼의 배열
result = 0  # 퀸을 놓을 수 있는 경우의 수
dfs(0)  # 0번째 행부터 시작
# print(result)  # 경우의 수 출력
