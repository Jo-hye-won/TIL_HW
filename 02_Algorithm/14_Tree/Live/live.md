## 트리
- 비선형 구조
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층 관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

- 한 개 이상의 노드로 이루어진 유한 집합이며 다음 조건을 만족한다
  - 노드 중 최상위 노드를 루트(root)라고 한다.
    - 나머지 노드들은 n(>=0)개의 분리집합 T1,...TN 으로 분리될 수 있다.
    

- 이들T1,...TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리라 한다.
 - 정점 : node, vertex 노드 혹은 버텍스라고 함
 - 단말노드 또는 잎노드

### 용어 정리
- 노드 : 트리의 원소
- 간선 : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
- 루트 노드 : 트리의 시작 노드
- 형제 노드 : 같은 부모 노드의 자식 노드들
- 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들

#### 차수(degree)
- 노드의 차수 : 노드에 연결된 자식 노드의 수
- 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
- 단말 노드(리프 노드) : 차수가 0인 노드, 자식 노드가 없는 노드

#### 높이
- 노드의 높이 : 루트에서 노드에 이르는 간선의 수, 노드의 레벨
- 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값, 최대 레벨

## 이진 트리
> 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개까지만 가질수 있는 트리
 - 왼쪽 자식 노드(left child node)
 - 오른쪽 자식 노드(right child node)

### 특성
- 레벨 n에서의 노드의 최대 개수는 2ⁿ개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며,
  최대 개수는 (2의 h+1승) -1 개가 된다.
  

### 종류
#### 1. 포화 이진 트리(Full Binary Tree) ★★★
> 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일 때, 최대의 노드 개수를 가진 이진 트리
  ex. 높이 3일 때 => 15개의 노드
  
- 루트를 1번으로 하여 (2의 h+1승) -1까지 정해진 위치에 대한 노드 번호를 가짐

#### 2. 완전 이진 트리(Complete Binary Tree) ★★★
> 높이가 h이고 노드 수가 n개일 때, 
> 포화 이진트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리

#### 3. 편향 이진 트리(Skewed Binary Tree)
> 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리


### 순회(traversal)
- 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말함
- 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결관계를 알 수 없다. 
- 따라서 특별한 방법이 필요
> 트리의 노드들을 체계적으로 방문하는 것

#### 3가지의 기본적인 순회방법
1. 전위순회(VLR) : 부모노드 방문 후, 자식노드를 좌,우 순서로 방문한다.
 - 수행방법 
    1) 현재 노드 n을 방문하여 처리한다 -> V
    2) 현재 노드 n의 왼쪽 서브트리로 이동한다 -> L
    3) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R
     
 - 전위 순회 알고리즘
```python
def preorder_traverse(T):
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)
```
☆★☆ 서브트리의 루트에서부터 순회하는것도 가능 : 그 트리안에서만 하고 위로 올라가지 않는다!!! ★☆★
        - 어디에서든지 시작해서 순회할 수 있다. 


2. 중위순회(LVR) : 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문한다.
 - 수행방법 
    1) 현재 노드 n의 왼쪽 서브트리로 이동한다 -> L
    2) 현재 노드 n을 방문하여 처리한다 -> V
    3) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R

 - 중위 순회 알고리즘
```python
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T) # 왼쪽에서 돌아오면 그 때 처리하는 !
        inorder_traverse(T.right)
```

3. 후위순회(LRV) : 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문한다.
 - 수행방법 
    1) 현재 노드 n의 왼쪽 서브트리로 이동한다 -> L
    2) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R 
    3) 현재 노드 n을 방문하여 처리한다 -> V

 - 후위 순회 알고리즘
```python
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T) 
```

### 이진트리의 표현 - 배열
- 노드 번호의 성질
 - 노드 번호가 i인 노드의 부모 노드 번호 : └i/2┙
 - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2*i
 - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2*i+1
 - 레벨 n의 노드 번호 시작 번호 : 2의 n승

> 트리는 간선보다 정점이 하나 더 많다.!!

### 이진트리의 저장
- 부모 번호를 인덱스로 자식 번호를 저장
> 참고 : 1번이 루트라는 보장은 포화이진트리와 완전이진트리일때 뿐이다.!!!★

- 자식 번호를 인덱스로 부모 번호를 저장
    : 루트만 부모번호가 없음
    : 루트나 조상 찾는 작업하기에 좋음
  
- 루트 찾기, 조상 찾기
```python
c = 5
while a[c] != 0:
    c = a[c]
    anc.append(c)
root = c
```

