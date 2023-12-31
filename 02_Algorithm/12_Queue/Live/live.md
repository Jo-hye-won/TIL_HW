# 큐
> 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
- 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
- 선입선출구조 : 큐에 삽입한 순서대로 원소가 저장되어, 
  가장 먼저 삽입된 원소는 가장 먼저 삭제된다.
  
- enQueue(item) : 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산
- deQueue() : 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
- createQueue() : 공백상태의 큐를 생성하는 연산
- isEmpty() : 큐가 공백상태인지를 확인하는 연산
- isFull() : 큐가 포화상태인지를 확인하는 연산
- Qpeek() : 큐의 앞쪽(front)에서 원소를 삭제없이 반환하는 연산

## 큐의 연산 과정
1. 공백 큐 생성 : createQueue()
   Q = [0]*100
   front = -1
   rear = -1
   => 아직 데이터가 하나도 돌아오지 않은 초기상태
   
2. 원소 A 삽입 : enQueue(A)
   rear += 1
   Q[rear] = A  
   
3. 원소 B 삽입 : enQueue(B)
4. 원소 반환/삭제 : deQueue()
5. 원소 C 삽입 : enQueue(C)
6. 원소 반환/삭제 : deQueue()
7. 원소 반환/삭제 : deQueue()

## 큐의 구현
### 선형큐
- 1차원 배열을 이용한 큐
- 큐의 크기 = 배열의 크기
 - 머리(front) : 저장된 첫 번째 원소 또는 마지막 삭제된 위치(인덱스)
 - 꼬리(rear) : 저장된 마지막 원소의 인덱스
- 상태 표현
 - 초기 상태 : front = rear = -1
 - 공백 상태 : front == rear
 - 포화 상태 : rear == n-1 (n:배열의 크기, n-1:배열의 마지막 인덱스)

> 초기 공백 큐 생성 : 크기 n인 1차원 배열 생성, front와 rear를 -1로 초기화
 
### 삽입 : enQueue(item)
- 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
1) rear값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
```python
def enQueue(item):
    global rear
    if isFull() : print("Queue_Full") <- 디버깅용
    else:
        rear <- rear + 1
        Q[rear] <- item
```


### 삭제 : deQueue(item)
- 가장 앞에 있는 원소를 삭제하기 위해
 1) front 값을 하나 증가시켜 큐에 남아있게 될 첫 번째 원소 이동
 2) 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함
```python
def deQueue(item):
    if(isEmpty()) then Queue_Empty()
    else{
        front  <- front +1;
        return Q[front];
    }
```

### 공백상태 및 포화상태검사 : isEmpty(), isFull()
- 공백상태 : front == rear
- 포화상태 : rear == n-1(n:배열의 크기, n-1: 배열의 마지막 인덱스)
```python
def isEmpty():
   return front == rear

def Full():
    return rear == len(Q) -1
```

### 검색 : Qpeek()
- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환
```python
def Qpeek():
    if isEmpty() : print("Queue_Empty")
    else : return Q[front+1]
```

### 잘못된 포화상태 인식
- 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는
공간이 있음에도 불구하고, rear = n-1 인 상태 즉, 포화상태로 인식하여 더 이상의 삽입을
  수행하지 않게 됨
  
> 해결방법
> 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형형태의 큐를 이른다고 가정


## 원형 큐의 구조
- Index의 순환
  - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 
    그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
    - 이를 위해 나머지 연산자 mod를 사용
   
- front변수
  - 공백상태와 포화 상태 구분을 쉽게 하기 위해 
    front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
    

## 우선순위 큐
- 특성
 - 우선순위를 가진 항목들을 저장하는 큐
 - FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다
- 적용분야
 - 시뮬레이션 시스템
 - 네트워크 트래픽 제어
 - 운영체제의 데스크 스케줄링

   
## 큐의 활용 : 버퍼(Buffer)
- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다.
