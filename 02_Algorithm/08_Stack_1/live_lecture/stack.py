# # stack class 직접 구현
#
class Stack:
#     # Stack 자료구조를 생성하는 순간, 기입해야 하는 정보들
#     # 지금 생성한 stack의 크기
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        # 최초 생성시의 top 위치
        self.top = -1   # -1은 맨 뒤 아님(파이썬의 negative indexing 일 뿐)(없음을 의미)

    # 1. stack이 비었는지
    def is_empty(self):
        '''
        stack이 비었을 때 pop 메서드가 실행되면
        현재 stack이 비어있음을 알려줄 수 있어야 해서 만들어주는 함수
        '''
        if self.top == -1:
            return True
        else:
            return False


    # 2. stack이 가득 찼는지
    def is_full(self):
        '''
           stack이 가득 찼을 때 push 메서드가 실행되면
           현재 stack이 가득 찼음을 알려줄 수 있어야 해서 만들어주는 함수
        '''
        if self.top + 1 == self.size:
            # if self.top == self.size -1:
            return True
        else:
            return False

    # 3. 값 삽입
    def push(self, item):
        # stack이 가득 찼을대는 들어갈 수 없어야 한다.
        if self.is_full():
            raise Exception('stack이 가득 찼어요.')  # 예외처리
        else:
            self.top += 1
            self.items[self.top] = item


    # 4. 값 제거
    def pop(self):
        if self.is_empty():
            raise Exception('stack에 값이 없어요!')
        else:
            value = self.items[self.top]
            self.items[self.top] = None  # 이거 안하면 ['A', None, None]이 나옴 ->> pop했는데 왜???
            self.top -= 1
            return value


    # 5. top 위치의 값 출력
    def peek(self):
        # stack이 비어있지 않다면
        if self.is_empty():
            raise Exception('stack에 값이 없어요!')

        # top번째 위치에 삽입되어 있는 값을 반환
        else:
            return self.items[self.top]

s1 = Stack(3)
print(s1.items)
print(s1.top)
print(s1.is_empty())
print(s1.is_full())
# print(s1.peek())
print("====='A'삽입=====")
s1.push('A')
print(s1.items)
print(s1.top)
print(s1.peek())

print("====='A'제거=====")
s1.pop()
print(s1.items)
print(s1.top)


