import sys
sys.stdin = open('input.txt')

T = 10
W = 100 # 가로는항상 100으로 주어짐

for tc in range(1, T+1):
    dump_ = int(input()) # 덤프 횟수 제한
    boxes = list(map(int, input().split())) # 각 상자의 높이
    result = 0
    while dump_ > 0: # 덤프횟수가 소진될 때까지
        dump_ -= 1 # 한번 반복할 때마다 덤프횟수 -1
        max_idx = 0
        min_idx = 0
        # 범위설정 1부터 하는 이유는 이미 max_idx 값 초기화를 0으로 해뒀기 때문에
        # 굳이 0부터 비교하면 똑같은거끼리 비교하는거라서 1부터 하면 되는 거!!
        for i in range(1, W):
            # boxes의 몇번째인덱스위치가 최고점일까
            if boxes[max_idx] <= boxes[i]:
                max_idx = i
            # boxes의 몇번째인덱스위치가 최저점일까
            if boxes[min_idx] >= boxes[i]:
                min_idx = i
        # 최고점 최저점을 찾은 다음에
        if boxes[max_idx] - boxes[min_idx] <= 1:
            # 최고점과 최저점의 간격이 1보다 작거나 같아지면(평탄화 완료)
            # 최고점과 최저점의 차이를 반환하고 끝낸다.
            result = boxes[max_idx] - boxes[min_idx]
            break
        else: # 평탄화가 완료되지 않으면(아직 진행중이면)
            boxes[max_idx] -= 1 # 가장 높은 상자에서 하나 빼서
            boxes[min_idx] += 1 # 가장 낮은 상자에 하나 더해주기

    if dump_ == 0: # 아직 평탄화 다 못했는데 평탄화제한 횟수 다 써버리면
        min_idx = 0
        max_idx = 0
        for j in range(W): # 범위 돌면서 최고점, 최저점 찾기
            # boxes의 몇번째인덱스위치가 최고점일까
            if boxes[min_idx] > boxes[j]:
                min_idx = j
            # boxes의 몇번째인덱스위치가 최저점일까
            if boxes[max_idx] <= boxes[j]:
                max_idx = j
        result = boxes[max_idx] - boxes[min_idx] # 그때의 차이 출력

    print(f'#{tc} {result}')