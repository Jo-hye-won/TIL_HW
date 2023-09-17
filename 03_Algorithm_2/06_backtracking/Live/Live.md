# 분할정복
> 학습목표
- 문제를 분할해서 해결하는 분할정복 기법을 이해하고 대표적인 알고리즘은 퀵 정렬과 병합 정렬에 대해 학습한다. 
- 상태 공간 트리의 모든 노드를 검색하는 백트래킹에 대해 학습한다.
- 이진트리(Binary Tree)의 특성을 이해하고 이진 트리의 중요한 연산인 탐색, 삽입, 삭제 알고리즘을 학습한다. 

## 유래
- 1805년 12월 2일 아우스터리츠 전투에서 나폴레옹이 사용한 전략
- 전력이 우세한 연합군을 공격하기 위해 나폴레옹은 연합군의 중앙부로 쳐들어가 연합군을 둘로 나눔
- 둘로 나뉜 연합군을 한 부분씩 격파함

## 설계 전략
### 1. 분할(Divide) 
: 해결할 문제를 여러 개의 작은 부분으로 나눈다.
### 2. 정복(Conquer)
: 나눈 작은 문제를 각각 해결한다. 
### 3. 통합(Combine) 
: (필요하다면) 해결된 해답을 모은다. 

## 거듭제곱
- 반복 알고리즘 : O(n)
```bash
literative_Power(x,n)
 result <- 1
 
 FOR i in 1 -> n
 	result <- result * x
  
 RETURN result
```

- 분할 정복 기반의 알고리즘 : O(log₂n)
```bash
Recursive_Power(x, n)
	IF n == 1 : RETURN x
    IF n is even
    	y <- Recursive_Power(x, n/2)
        RETURN y * y
    ELSE
    	y < Recursive_Power(x, (n-1)/2)
        RETURN y * y * x
```

## 병합정렬(Merge Sort)
> 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - top-down 방식
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
 - 시간 복잡도 : O(n log n)

```bash
# 분할 과정
merge_sort(LIST m)
	IF length(m) ==1 : RETURN m
    
    LIST left, right
    middle <- length(m) / 2
    FOR x in m before middle
   		add x to left
    FOR x in m after or equal middle
    	add x too right
    
    left <- merge_sort(left)
    right <- merge_sort(right)
    
    RETURN merge(left, right)
```

```bash
# 병합 과정
merge_sort(LIST left, LIST right)
	LIST result
    
    WHILE length(left) > 0 OR length(right) > 0
    	IF length(left) > 0 AND length(right) > 0
        	IF first(left) <= first(right)
            	append popfirst(left) to result
            ELSE
            	append popfirst(right) to result
        ELIF lengt(left) > 0
        	append popfirst(left) to result
        ELIF lengt(right) > 0
        	append popfirst(right) to result
    RETURN result
```

# 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다
- 병합정렬과 다른점
	- 병합정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item)중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다.
    - 각 부분 정렬이 끝난 후, 병합정렬은 '병합'이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다. 

## 아이디어
- P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다.
- 피봇을 두 집합의 가운데에 위치시킨다. 
- 피봇 선택 : 왼쪽 끝/오른쪽 끝/임의의 세개 값 중에 중간 값    


## 알고리즘 

```bash
quickSort(A[], l, r)
    if l < r
        s <- partition(a, l, r)
        quickSort(A[], l, s - 1)
        quickSort(A[], s + 1, r)
```

    
```bash
# Hoare-Partition 알고리즘
quickSort(A[], l, r)
    p <- A[l] # p : 피봇 값
    i <- l, j <- r
    WHILE i <= j
        WHILE i <= j and A[i] <= p : i ++
        WHILE i <= j and A[j] >= p : j --
        IF i < j : swap(A[i], A[j])
    # 왜 i와 j가 교차하나??
    # i,j는 피봇을 기준으로 작은 값과 큰 값들의 경계에 위치해서 
    swap(A[l], A[j])
    RETURN j
```

```bash
# Lomuto partition 알고리즘
quickSort(A[], p, r)
    x <- A[r] 
    i <- p - 1
   
    FOR j in p -> r - 1
        IF A[j] <= x
            i++, swap(A[i], A[j])
    
    swap(A[i+1], A[r])
    RETURN i + 1
```


# 이진 검색(Binary Search)
> 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다. 

## 검색과정
1. 자료의 중앙에 있는 원소를 고른다. 
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다. 


## 알고리즘

```bash
# 반복구조
binarySearch(n, S[], key)
low = 0
high = n - 1 

while low <= high:
    mid = low + (high - low) / 2

    if S[mid] == key:
        return mid
    elif S[mid] > key:
        high = mid - 1 
    else:
        low = mid + 1
return -1
```

```bash
# 재귀구조
binarySearch(a[], low, high, key)
    if low > high
        return -1
    else
        mid = (low + high) / 2
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            return binarySearch(a[], low, mid - 1 , key)
        else:
            return binarySearch(a[], mid + 1, high, key)
```

## 분할 정복의 활용
- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘이다. 또한, 멀티코어(Multi-Core) CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용된다.
- 퀵 정렬은 매우 큰 입력 데이터에서 좋은 성능을 보이는 알고리즘이다. 


# 백트래킹
> 여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지를 선택한다.

- 선택이 이루어지면 새로운 선택지들의 집하이 생성된다.
- 이런 선택을 반복 하면서 최종 상태에 도달한다. 
 - 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.

## 당첨 리프 노드 찾기
- 루트에서 갈 수 있는 노드를 선택한다.
- 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작한다.
- 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다. 
- 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다. 

## 백트래킹과 깊이 우선 탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 다라가지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
- 깊이 우선 탐색이 모든 경로를 추적하는데 비해  백트래킹은 불필요한 경로를 조기에 차단.
- 깊이 우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉,  N!가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
- 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능

- 루트 노드에서 리프노드까지의 경로는 해답후보가 되는데, 깊이우선 검색을 하여 그 해답후보 중에서 해답을 찾을 수 있다. 
- 그러나 이 방법을 사용하면 해답이 될 가능성이 전혀 없는 노드의 후손 노드들도 모두 검색해야 하므로 비효율적이다.

### 백트래킹 기법
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌가 다음 자식 노드로 감.
- 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다. 
- 가지치기(prunning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다. 

# 트리
