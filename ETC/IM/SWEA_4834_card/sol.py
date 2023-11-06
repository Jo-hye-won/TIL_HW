import sys
sys.stdin = open('input.txt')
'''
가장 많은 카드에 적힌 숫자와
카득 몇 장인지 출력하는 프로그램
카드 장수가 같을 때는 적힌 숫자가 큰 쪽 출력
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 10  # 카드 개수 체크할 배열
    # print(cnt)
    cards = list(map(int, input()))
    # print(cards)
    for i in cards:
        cnt[i] += 1
    # print(cnt)
    max_card = 0
    for j in range(len(cnt)):
        if max_card <= cnt[j]:
            max_card = cnt[j]
            index = j
    print(f'#{tc} {index} {max_card}')
