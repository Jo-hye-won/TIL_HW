'''
# 일단 직선으로 N크기만큼 간다음에
# 앞이 막혀있거나 배열의 끝이면
앞이 막혀있는걸 알게 하려면 0으로 채워진 배열을 만들어두고
숫자가 입력되면 그 위치의 배열의 수가 1이 되게 만들어야 함
 while 벽을 만날 때 종료하겠다.

회전은 우 - 하 - 좌 - 상 순으로 반복됨

배열에 넣어야 할 숫자는 1 - N**2

for 어떤 조건 동안 : 몇 번 시행될지 알 때
while 종료조건 : 몇 번 시행될 지 모를 때
'''

T = int(input())
    # 우 하  좌  상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    P = 2  # 숫자를 1씩 늘려가면서 더해줄 거라서 1을 P로 해두고
    ni, nj = 0, 0
    k = 0
    arr[0][0] = 1
    while P != N**2 + 1:  # 숫자를 다 적을 때까지 36까지는 적히고 37부터 끝
        ni += di[k % 4]
        nj += dj[k % 4]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = P  # 시작은 P로 시작한다.
            P += 1   # 시작과 함께 다음에 넣을 P값은 1 증가

        else:  # 벽을 만나면 한칸 뒤로 물러났다가 회전시키기(k+=1)
            ni -= di[k % 4]
            nj -= dj[k % 4]
            k += 1
    print(f'#{tc}')
    for ls in arr:
        print(*ls)


    # for i in range(N):
    #     for j in range()

