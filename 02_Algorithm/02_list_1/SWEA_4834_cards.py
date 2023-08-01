import sys
sys.stdin = open('card.txt')

# 숫자 카드
 T = int(input())       # 테스트 케이스 개수
 N = int(input())       # 카드 장수

 card = list(map(int, list(str(input())))) # 카드의의
