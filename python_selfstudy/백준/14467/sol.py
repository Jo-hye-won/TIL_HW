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

N = int(sys.stdin.readline())
place = [7]*11 # 0과 1이 아닌 값으로 리스트 만들어두고
# print(place)
cnt = 0
for i in range(N):
    cow, where = map(int, sys.stdin.readline().split())
    if place[cow+1] == 7:  # 7이면
        place[cow+1] = where # 소의 위치 입력해주고
    else:
        if place[cow+1] != where: # 소의 위치가 다를 때
            cnt += 1 # 소가 길을 건넌 횟수 증가시켜 주고
            place[cow+1] = where # 위치 변환시켜주기
print(cnt)
