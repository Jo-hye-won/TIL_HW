import sys
sys.stdin = open('card.txt')
'''
가장 많은 카드의 숫자와 장 수를 차례로 출력
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = map(int, input())
    tmp = [0] * 10
    for card in cards:
        tmp[card] += 1

    max_card = tmp[0]  # 초기값 설정
    for index in range(len(tmp)):
        if max_card <= tmp[index]:
            max_card = tmp[index]
            card_count = index
    print(f'# {tc} {card_count} {max_card}')


    # for i in tmp:
    #     if max_card <= i:   # 초기값보다 i가 크면 i로 바꾸기
    #                         # 만약 같아도 뒤의 큰 값으로 출력해야하기 때문에 이상
    #         max_card = i
    # print(max_card)
