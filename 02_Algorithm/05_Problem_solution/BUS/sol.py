# 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt')

T = int(input())
# station = [0] * 5000      # 카운트 배열만들어두고
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5001         # 1-5000번 각 정류장을 지나는 노선수 카운트 배열만들어두고
    for _ in range(N):       # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A, B+1):
            cnt[i] += 1

    #                 0  1  2  3  4  5  6  7  8  9  10 ...
    # print(cnt)   # [0, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ...]

    P = int(input())  # 정류장 개수
    bus_stop = [int(input())for _ in range(P)]      # 각 정류장 번호

    # print(bus_stop)    # 첫번째 테스트 케이스에서는 # [1, 2, 3, 4, 5]
    print(f'#{tc}', end=' ')  # 출력 # 나와야해서 이거먼저 입력해주고
                              # 뒤에 공백주고
                              # 이어서 밑에서 cnt[x]를 출력해줄것임

    # 버스 정류장 [1, 2, 3, 4, 5] 위치의 노선수를 가져오자
    for x in bus_stop:  # x는 cnt로 몇개의 노선이 가는지 구해둔 cnt 리스트에 접근하기 위한
                        # 버스정류장 번호이자, 리스트인덱스 번호가 됨
        print(cnt[x], end=' ')

    print()  # 줄바꿈 처리 해줘야 함! 안그러면 다른 테스트케이스가 한줄로 쭉 연결되기 때문에 fail뜬다.
    print(68)  # 줄바꿈처리 해줬기 때문에 이제 아래 줄에 출력됨


    # # for x in bus_stop:      # bus_stop = [1, 2, 3, 4, 5]으로 버스정류장의 번호가 x에 들어가고
    #                     # x는 cnt로 몇개의 노선이 가는지 구해둔 리스트에 접근하기 위한 리스트

        # print(f'#{tc}', end =' ')     # cnt의 x인덱스위치에 있는 노선의 개수 뽑아서 중간중간에 공백주면서 프린트
        # print(f'{cnt[x]}', end =' ')
        # print(f'#{tc}', *bus_stop)