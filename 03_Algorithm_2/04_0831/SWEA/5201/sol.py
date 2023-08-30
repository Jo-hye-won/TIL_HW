import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))
    matrix = list(map(int, input().split()))

    # 화물은 하나씩 담을수 있으니까 가장 큰화물을 가장 큰 트럭에 담는것이 최고
    # 이를 위해 무게와 용량을 큰 순서대로 정렬
    sort_goods = sorted(goods, reverse=True)
    sort_matrix = sorted(matrix, reverse=True)

    # 결과값 초기화(트럭 수만큼)
    result = [0 for _ in range(M)]

    # 화물들을 번갈아 가면서 넣어본다.
    for i in range(N):
        # 화물에 맞는 트럭을 검사한다.
        for j in range(M):
            # 만약 화물을 적재할 수 있을 때
            if sort_goods[i] <= sort_matrix[j]:
                # 그 트럭에 아무것도 실려있지 안하면
                if not result[j]:
                    # 트럭에 적재를 한다
                    result[j] = (sort_goods[i])
                    # 그리고 이 짐은 이미 실렸기 때문에 break하여 다음 짐을 본다
                    break
    print(f'#{tc} {result}')