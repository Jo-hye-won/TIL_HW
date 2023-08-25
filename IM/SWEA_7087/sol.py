import sys
sys.stdin = open('input.txt')

'''
대회의 문제들에 사용될 수 있는 재목을  N개 만듬

'''
T = int(input())
cnt = 0  # 최대 문제 제목의 개수를 세는 변수

for tc in range(1, T+1):
    N = int(input())
    words = list(input() for _ in range(N))
    print(words)