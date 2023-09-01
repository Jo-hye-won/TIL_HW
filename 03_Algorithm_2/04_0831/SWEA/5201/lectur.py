import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    TR = list(map(int, input().split()))

    # 1. 화물을 옮기려면, 트럭이 필욯다.
    # 2. 트럭이 있어봤자, 화물이 없으면 의미 없다.
    # 3. 트럭은 편도로 이동한다. => 한번 가면 끝
    # 4. 화물도 편도로 이동한다. => 한번 가면 끝
    # 5. 최대한 내가 들 수 있는 제일 무거운 화물을 들고간다.
    W.sort()
    TR.sort()
    print(W, TR)
    result = 0
    while W and TR:
        if TR[-1] >= W[-1]:
            TR.pop()
            result += W.pop()
        else:
            W.pop() # 버려버리기
    print(f'#{tc} {result}')
