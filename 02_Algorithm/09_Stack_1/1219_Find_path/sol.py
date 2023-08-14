import sys
sys.stdin = open('input.txt')


def DFS(node):
    stack = [node]  # 스택에 받아오는 값(출발점) 넣고
    visited = [0] * 100  # 방문 표시할 리스트(0에서 99까지 표시해줘야 해서 100개 만듬)
    visited[node] = 1  # 출발시작하니까 방문한거라서 1로 표시해주고

    while stack:    # 스택에 값이 있는 동안
        now = stack.pop()  # 시작노드를 스택의 젤 위에 있는 값 받아와서 함

        for next in range(100):  # 배열의 크기가 100이라서 범위를 100으로 줬음

            # 노선이 그어져 있는지 확인 할 수 있는 배열의 값이 1이고(갈수있다고 되어있고)
            # visited[next] 값이 0이면(아직 방문한 적 없다고 되어있다면)
            if arr[now][next] == 1 and visited[next] == 0:
                stack.append(next)  # next를 스택에 넣어주자

                # 필요 없음. # start = next  # 그리고 next가 다음 스타트가 되어야 한다.

                # 그리고 방문했으니까 visited 값도 1로 바꿔주자
                visited[next] = 1

            if now == goal:  # 노드가 goal인 99가 되었을 때(99에 다다랐다는 뜻)
                return 1  # 1을 리턴하고
    else:
        return 0  # while 다 돌고


T = 10
# start = 0   # 출발점
# goal = 99   # 도착점

for tc in range(1, T+1):
    start = 0  # 출발점
    goal = 99  # 도착점
    t, N = map(int, input().split())
    # 출발점 + 도착점 + 정점 합해서 100개라서 크기가 100인 배열을 만들기
    arr = [[0] * 100 for _ in range(100)]
    numbers_list = list(map(int, input().split()))

    # numbers_list에서 홀수번째 꺼내와서 arr의 행(i)인덱스번호로
    #     # numbers_list에서 짝수번째 꺼내와서 arr의 열(j)인덱스번호로 쓸래
          # 이렇게 이중포문 쓰면 이상해짐  # 아래와 같이 표현하면 됨
    for i in range(0, N * 2, 2):
        arr[numbers_list[i]][numbers_list[i+1]] = 1


    print(f'#{tc} {DFS(start)}')





    # print(f'#{tc} {arr}')

# for tc in range(1, T+1):
#     t, N = map(int, input().split())  # t는 테스트케이스인데 어차피 tc쓸거라서 안쓸거임
#                                       # N은 길의 총 개수
#
#     arr = [[0] * 100 for _ in range(100)]
#     # print(arr)
#     # arr2 = [[0] * 100 for _ in range(100)]
#     numbers_list = list(map(int, input().split()))  # 노드연결 시작점, 끝점
#     # print(numbers_list)
#                     # 배열 두개 만들어서 하나는 앞에꺼 range(0, N*2, 2)
#                     # 하나는 뒤에꺼 range(1, N*2, 2) 표시하게 만들자
#                     # 배열 두개 만들어서 하나는 앞에꺼 range(0, N*2, 2)
#                     # 하나는 뒤에꺼 range(1, N*2, 2) 표시하게 만들자
#                     # for i in range(2):
#
#     # numbers_list에서 홀수번째 꺼내와서 arr의 행(i)인덱스번호로
#     # numbers_list에서 짝수번째 꺼내와서 arr의 열(j)인덱스번호로 쓸래
#
#     for i in range(0, N*2, 2):
#         # print(numbers_list[i])
#         for j in range(1, N*2, 2):
#             # print(numbers_list[j])
#             arr[numbers_list[i]][numbers_list[j]] = 1
#     print(f'#{tc} {arr}')