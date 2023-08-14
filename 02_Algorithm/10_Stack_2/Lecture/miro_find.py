
# 체크할 배열
# 시작점(현재 조사 위치 now)
# 종료지점(모든 원소의 개수가 종료시점 == N)(end)
# 총합 : 누적값 acc(result)

def solution(arr,end, result):
    # 부분집합의 합이 10인 경우
    if result != 10:
        return
    for i in range(1, end +1):
        if arr[i]:
            print(data[i], end=' ')
    print()


def construct_candidates(c):
    c[0] = True    # 쓴다
    c[1] = False   # 안쓴다
    return c


def backtracking(arr, now, end, result):
    global count
    if result > 10:   # pruning
        return
    count += 1
    # 후보군 목록
    # 부분집합의 원소로 now번째의 값을 쓸거냐 안쓸거냐 (T/F)
    c = [0] * 2

    # 언제까지 조사를 할것이냐
    if now == end:
        solution(arr, end, result)  # 값을 도출하는 함수를 호출
    else:
        # 아직 조사해야 하는 원소가 남았다.
        # 다음 원소를 조사하러 가기 위해 index 1 증가
        now += 1
        # now가 1 증가된 다음 해야할 것
        # 내가 arr[now] 값을 쓸지 말지를 판별할 수 있는 후보군 만들기
        # arr, 지금까지 사용한 원소 인덱스, 최대 원소 개수, 후보군 목록에 기록
        ncandidates = construct_candidates(c)
        # 후보군 수 만큼 반복해서 조사
        for i in range(len(ncandidates)):
            arr[now] = c[i]
            if arr[now]: #현재 조사하고 있는 대상 쓰기로 했으면
                # now번재 원소 쓰기로 했으면
                # 부분집합의 합의 누적 값이 now번째 원소의 값 만큼 증가
                backtracking(arr, now, end, result+data[now])
            else:
                # now번째 요소를 안쓴 날
                backtracking(arr, now, end, result)



# 유망성(다음조사를 하는 의미가 있니 없니?)
# 후보군 수 :우리의 후보군이란,  0과 1밖에 없다. (쓰거나 안쓰거나/ 넣거나 안넣거나)
# MAXCANDIDATES = 12  그래서 우린 지금은 이거 안쓸거다

# 최대 원소 개수
NMAX = 12  # 넉넉하게 하나정도 더 넣어줌
count = 0

data = list(range(11))
arr = [0] * NMAX  # 각 원소를 사용할 것이냐 말 것이냐를 체크할 배열
# [1,2,3,4] 일때,
# arr = [0,1,1,1,1,0,0,0,0,0,0]
backtracking(arr, 0, 10, 0)  # 총합 0에서 시작해야 더하지
print(count)