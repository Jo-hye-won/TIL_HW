import sys


def electric_bus(K, N, M, chargers):
    count = 0
    current = 0

    while True:
        if current + K >= N:  # 현재 위치에서 최대 이동 가능 거리를 더한 값이 종점을 지나면
            return count  # 충전 횟수 반환
        else:
            for charger in reversed(chargers):
                # 현재 위치에서 최대 이동 가능 거리를 더한 값 사이에 충전소가 있으면
                if current + 1 <= charger <= current + K:
                    count += 1  # 충전 횟수 증가
                    current = charger  # 현재 위치 갱신
                    break  # for 문 종료
            else:  # for 문이 break 없이 종료되었다면 이동 거리 내 충전소가 없다는 뜻.
                return 0  # 실패


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    print(f'#{tc} {electric_bus(K, N, M, chargers)}')





