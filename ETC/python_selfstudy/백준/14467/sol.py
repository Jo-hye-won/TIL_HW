import sys
sys.stdin = open('input.txt')
'''
소의 위치를 N번 관찰하는데, 
각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있음
소 10마리
소의 위치 = 0 / 1 

소가 최소 몇 번 길을 건넜는지
같은 번호의 소가 위치를 바꾼 것이 몇 번인지?
'''

N = int(input())
place = [7]*12 # 소가 10마리라서 인덱스 오류 안나게 하려고 12개로 만들었음
# print(place)
cnt = 0
for i in range(N):
    cow, where = map(int, input().split())
    if place[cow+1] == 7:  # 7이면 # place를 11로 했었다면 이거 인덱스 cow로 해야함
        place[cow+1] = where # 소의 위치 입력해주고
    else:
        if place[cow+1] != where: # 소의 위치가 다를 때
            cnt += 1 # 소가 길을 건넌 횟수 증가시켜 주고
            place[cow+1] = where # 위치 변환시켜주기
print(cnt)
