N = int(input())
for k in range(1, N + 1):
    arr = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 입력
    rowArr = arr #가로 배열은 입력받은 배열과 동일
    colArr = [[arr[i][j] for i in range(9)] for j in range(9)] #새로 배열 변환
    sqrArr = [[arr[i % 3 * 3 + j // 3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)] # 3 * 3 사각형 각각을 1차원 배열로 변환
    answer = 1 #출력할 정답
    for row, col, sqr in zip(rowArr, colArr, sqrArr): # 2차원배열에서 각각 1차원 배열을 꺼내서
        if len(set(row)) == len(set(col)) == len(set(sqr)) == 9: # 집합으로 변환했을때 길이가 모두 9이면
            continue # 통과
        else: #아니면 (스도쿠 조건 충족 X)
            answer = 0 #정답 0으로 설정
            break # 반복 중단
    print("#", k, " ", answer, sep="") #정답 출력