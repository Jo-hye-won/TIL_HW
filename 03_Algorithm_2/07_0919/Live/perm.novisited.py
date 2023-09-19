# 순열
# r : 내가 사용하고 있는 값의 수

def perm(r):
    # 재귀 함수
    # 종료 조건(재귀의 기저까지 왔을 때의 상황)
    if r == N:
        # 내가 원하는 무언가를 실행
        return
    else:
        # 내가 가진 arr의 모든 원소를 매번 사용할 것인지 체크
        for i in range(N):
            # arr의 i번째 요소를 쓴 적이 있는지 없는지를 기준으로 판단

            perm(r+1)


# nPr : n개의 요소 중, r개를 사용하여 순열
arr = [1, 2, 3]
N = len(arr)

# 최종적으로 완성될 순열을 담아 둘 리스트
completed_perm = [0] * N