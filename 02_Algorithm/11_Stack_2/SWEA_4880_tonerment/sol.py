import sys
sys.stdin = open('input.txt')
'''
1 = 가위
2 = 바위
3 = 보

'''
def cards_game(start, end):  #
    if start == end:
        return start
    mid = (start + end) // 2
    left = cards_game(start, mid)
    right = cards_game(mid+1, end)
    return rock_paper(left, right)


def rock_paper(left, right):
    if cards[left] == cards[right]:
        return left
    elif cards[left] - cards[right] == 1 or cards[left] - cards[right] == -2:
        return left
    return right


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc} {cards_game(0, N-1)+1}')