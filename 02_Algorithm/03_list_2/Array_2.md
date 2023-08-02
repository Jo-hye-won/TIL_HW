## 배열 2(Array 2)

### 2차원 배열의 선언
- 1차원 list를 묶어놓은 list
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

N=int(input())
arr = [list(map(int, input().split()))for _ in range(N)] 
-> list(map(int, input().split()))를 N번 반복하도록 해

N=int(input())
arr = [list(map(int, input()))for _ in range(N)]

### 배열 순회
- n * m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

### 행 우선 순회 (->)
```python
# i행의 좌표
# j열의 좌표
for i in range(n):
  for j in range(m):
    f(Array[i][j])   # 필요한 연산 수행
            행 열
```


### 열 우선 순회
```python
# i행의 좌표
# j열의 좌표

for j in range(m): # 열
  for i in range(n):   # 행
    f(Array[i][j])   # 필요한 연산 수행
    
for i in range(n): # 행
  for j in range(m):   # 열
    f(Array[j][i])   # 필요한 연산 수행
            
```

### 지그재그 순회(짝수는 오른쪽으로 홀수는 왼쪽으로 순회)
```python
# i행의 좌표
# j열의 좌표
for i in range(n):
  for j in range(m):
    f(Array[i][j+(m-1-2*j)*(i%2)])   # 필요한 연산 수행
    # (i%2) => 짝수번 행일때는 (m-1-2*j)이 날아가고
    # 홀수번 행일때는 (m-1-2*j)를 남겨두는 역할을 하게 됨 
```

### ★★★ 델타를 이용한 2차 배열 탐색 ★★★
> 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
- 그림그려두고 보면서 코드로 옮기는 것이 안전하고 편하다!!
-> IM의 단골 소재 ★★
```python
arr[0...N-1][0...N-1]   # NxN배열
di[] <- [0, 1, 0, -1]
         |  |  |   |
dj[] <- [1, 0, -1, 0]
for i : 0 -> N-1 :
  for j : 0 -> N-1 :
    for k in range(4) : # i,j에 대해서 4번 접근할거야
        ni  <- i + di[k]
        nj  <- j + dj[k]
        if 0 <= ni < N and 0 <= nj < N  # 유효한 인덱스면
                            # 유효한 범위를 벗어나지 않았는지 확인
                f(arr[ni][nj])

```
> 풍선팡은 델타탐색으로..

### 전치 행렬
> 대각선 기준으로 자리 바꾸는 거
> 
```python
# i행의 좌표, len(arr)
# j열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j :
            arr[i][j] , arr[j][i] = arr[j][i],arr[i][j]

```


### 연습문제 1
- 5x5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
- 25개의 각 요소에 대하여 그 요소와 이웃한 요소와의 차의 절대값을 구하시오
- 예를 들어 아래 그림에서 7 값의 이웃한 값은 2,6,8,12이며 차의 절대값의 합은 12
- 25개의 요소에 대해 모두 조사하여 총합을 구하시오
- 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오


## 부분집합 합(Subset Sum)
