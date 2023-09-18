#  알고리즘 설계 기법의 종류
1. 전체를 다 보자 (Brute Force - 완전 탐색)
    - 배열 : 반복문을 다 돌리기
    - 그래프 : DFS, BFS

2. 상황마다 좋은 걸 고르자(Greedy - 탐욕)
    - 규칙을 찾는 것
    - 주의사항 : 항상 좋은 것을 봅아도, 최종 결과가 제일 좋다는건 보장되지 않는다. 

3. 하나의 큰 문제를 작은 문제로 나누어 부분적으로 해결하자(DP-Dynamic Programming)
    - memoization 기법을 활용
    - 점화식(bottom-up)방법과, 재귀(top-down)방법이 있음

4. 큰 문제를 작은 문제로 쪼개서 해결하자(Divide and Conquer - 분할 정복)
5. 전체 중, 가능성 없는 것을 빼고 보자(Backtracking - 백트래킹)
    - 가지치기


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

# 병합정렬(Merge Sort)
> 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - top-down 방식
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
 - 시간 복잡도 : O(n log n)

1. 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속한다.
    - 더이상 나눌 수 없을때까지 나눠주기 
    - 정복 = 정렬을 한다는 것
2. 병합단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
    - 8개의 부분집하비 1개로 병합될 때까지 반복함


```bash
# 분할 과정
merge_sort(LIST m)
	IF length(m) == 1 : RETURN m # 길이가 1이 될때까지 나눠라
    
    LIST left, right
    middle <- length(m) / 2 # 가운데 
    FOR x in m before middle # 왼쪽
   		add x to left
    FOR x in m after or equal middle # 오른쪽
    	add x too right
    
    left <- merge_sort(left) 3 # 다시한번 재귀를 돌린다!
    right <- merge_sort(right)
    
    RETURN merge(left, right) # 하나의 정렬된 리스트로 반환해라
```

```bash
# 병합 과정
merge_sort(LIST left, LIST right)
	LIST result
    
    WHILE length(left) > 0 OR length(right) > 0  # 배열이 남아잇을 때까지 반복할건데 
    	IF length(left) > 0 AND length(right) > 0
        	IF first(left) <= first(right) # 왼쪽 젤 첨꺼 오른쪽 젤 첨꺼 비교해서 더 작은 것을
            	append popfirst(left) to result # result 배열에 넣어라 
            ELSE
            	append popfirst(right) to result
        ELIF lengt(left) > 0  # 남은 데이터를 모두 넣어라 
        	append popfirst(left) to result
        ELIF lengt(right) > 0
        	append popfirst(right) to result
    RETURN result
```

# 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다
- 병합정렬과 다른점
	- 병합정렬은 그냥 두 부분으로 나누는 반면에, 퀵 정렬은 분할할 때, 기준 아이템(pivot item)중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킨다. (나눌 때 추가적인 동작이 있다는 것)
    - 각 부분 정렬이 끝난 후, 병합정렬은 '병합'이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다. 

## 아이디어
- P(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 한다.
    P | P > 요소들 | 요소들 > P

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
# Hoare-Partition (호어파티션) 알고리즘 => i,j가 처음과 끝에 있다면
quickSort(A[], l, r)
    p <- A[l] # p : 피봇 값
    i <- l, j <- r
    WHILE i <= j
        WHILE i <= j and A[i] <= p : i ++
        WHILE i <= j and A[j] >= p : j --
        IF i < j : swap(A[i], A[j])
    # 왜 j와 피봇의 위치를 교환하는가? i와 j가 교차하면, i,j는 피봇을 기준으로 작은 값과 큰 값들의 경계에 위치해서 j의 위치가 피봇의 위치다
    swap(A[l], A[j])
    RETURN j
```

```bash
# Lomuto partition(로무토 파티션) 알고리즘 -> 호어에 비해서 안좋음 (이런게 있구나 정도만 이해하자)
# => i,j가 같이 진행한다면
quickSort(A[], p, r)
    x <- A[r] 
    i <- p - 1
   
    FOR j in p -> r - 1
        IF A[j] <= x
            i++, swap(A[i], A[j])
    
    swap(A[i+1], A[r])
    RETURN i + 1
```

### Hoare & Lomuto
- Lomuto = 같은 숫자가 많으면 필요없는 스왑이 많이 발생해버림!


# 이진 검색(Binary Search) => 코테 단골 유형!!! ★★
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


###  Today lecture arrangement
> sort(), sorted()와 같은 내장 라이브러리가 굉장히 강력!!

- 병합정렬 
  - 직접 구현할 일은 적다 
    -> 멀티 쓰레드 : 
  - 과거 면접 단골 질문 + 분할 정복 학습에 좋다 
  - 코드를 보기 전에 반드시 손으로 직접 해보기

- 퀵 정렬
  - 직접 구현할 일은 적다 
    -> 평균적으로 굉장히 좋은 알고리즘 (NlonN)
    -> 특히, 큰 데이터를 다룰 때 좋다.
    -> 단점 : 역순 정렬 등 최악의 경우 O(N^2)
  - 과거 면접 단골 질문 + 분할 정복 학습에 좋다 
  - 코드를 보기 전에 반드시 손으로 직접 해보기

- 이진 검색 
    - 코딩 테스트의 메인 알고리즘 중 하나
    - 목적 : "원하는 값을 빨리 찾는 것"
    - 시간 : O(logN)
    - Parametric Search
        - lower bound
        - upper bound
            - 여러 개의 데이터 중 2가 처음 나온 시점
            - 2-9 사이의 데이터는 몇개인가?