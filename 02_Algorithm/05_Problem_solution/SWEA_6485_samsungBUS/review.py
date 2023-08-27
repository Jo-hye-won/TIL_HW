# 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt')

'''
노선 N개
번호가 A이상이고 B이하인 모든 정류장만을 다닌다
P개의 버스정류장에 대해
각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램 작성
'''

T = int(input())
for tc in range(1, T+1):
    bus_cnt = [0] * 5001  # 버스 정류장 5000개 있어서 여유있게 5001개 만들
    N = int(input())
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_cnt[i] += 1  # 버스 노선 A-B까지가니까 들리는거 표시해주기
    # print(bus_cnt) # [0, 1, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0....
    P = int(input())
    bus_station = [int(input()) for _ in range(P)]  # [1, 2, 3, 4, 5]
    result = []
    for k in bus_station:
        ap = bus_cnt[k]
        result.append(ap)
    print(f'#{tc}', *result)
