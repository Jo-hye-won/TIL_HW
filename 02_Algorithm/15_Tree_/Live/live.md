## 수식 트리
- 수식을 표현하는 이진 트리
- 수식 이진트리라고 부르기도 함
- 연산자는 루트 노드이거나 가지노드
- 피연산자는 모두 잎 노드

## 이진 탐색 트리
- 탐색작업을 효율적으로 하기 위한 자료구조
- 모든 원소는 서로 다른 유일한 키를 갖는다.
 > key(왼쪽 서브트리) < key(루트 노드) < key(오른쪽 서브트리)
- 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리다.
- 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

### 탐색 연산
- 루트에서 시작한다
- 탐색할 키 값 x를 루트 노드의 키 값과 비교한다
    - (키 값 x= 루트노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 탐색 연산 성공
    
- 서브트리에 대해서 순환적으로 탐색 연산을 반복한다

### 삽입 연산
- 어 여기 있어야 하는데 없어 그럼 집어넣을거야
1. 먼저 탐색 연산을 수행
    - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인
    - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다. 
2. 탐색 실패한 위치에 원소를 삽입한다.

### 성능
- 탐색, 삽입, 삭제 시간은 트리의 높이 만큼 시간이 걸린다. 
- 평균의 경우 : lon n (이진트리가 균형적으로 생성되어 있는 경우)
- 최악의 경우 : 한쪽으로 치우친 경사 이진트리의 경우 : 순차탐색과 시간 복잡도가 길다. 
    -> 완전 이진 트리 또는 균형트리로 바꿀 수 있다면최악의 경우를 없앨 수 있다. 
        새로운 원소를 삽입할 때 삽입 시간을 줄인다


## 힙(heap)
> 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
> 키값이 가장 큰 노드나 가장 작은 노드를 찾기에 용이한 자료구조
> 
- 최대 힙 (max heap)
 : 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
  : 부모노드의 키값 > 자식노드의 키값
  : 루트 노드 : 키값이 가장 큰 노드
  
- 최소 힙 (max heap)
 : 키값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  : 부모노드의 키값 < 자식노드의 키값
  : 루트 노드 : 키값이 가장 큰 노드
  
- 
  

### 힙 연산 - 삽입
1. 완전 이진 유지
2. 부모>자식 유지

  
### 힙 연산 - 삭제
- 힙에서는 루트 노드의 원소만을 삭제할수 있다
- 루트 노드의 원소를 삭제하여 반환한다
- 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다.
1. 완전 이진트리 유지
```python
tmp = h[1]
h[1] = h[last]
last += 1
```
2. 최대합 유지(부모> 자식)

- 자식이 없거나 부모가 크면 비교 중지

   