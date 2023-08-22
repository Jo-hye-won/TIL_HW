'''
항상 완전 이진 트리를 유지
n+1개 배열 생성
last = 0
enque(7)

# 완전이진트리 유지
last += 1
h[last] = n

p = last//2
while p>0 and h[p] > h[c] # 최소힙에 위배
    h[p] <-> h[c] # 둘이 교환해
    c <- p
    p <- c//2
'''

def deq():
    global last
    tmp = heap[1]   # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1   # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식 (비교할 자식노드 번호)
    while c <= last:  # 자식이 하나라도 있으면...
        if c+1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1      # 비교 대상이 오른쪽 자식노드
        else:  # 부모가 더 크면
            break  # 비교 중단

    return tmp

heap = [0] * 100
last = 0  # 마지막 정점 번호
