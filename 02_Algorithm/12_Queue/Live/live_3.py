
def enQ(data):
    global rear
    if (rear+1) % cQsize == front:  # 꽉 찼으면
        # print('cQ is full')
    else:
        rear = (rear+1) % cQsize   # 값을 읽기만 할게 아니라 바꾸려면 글로번 선언
        cQ[rear] = data


def deq():
    global front
    front = (front+1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enQ(1)
enQ(2)
enQ(3)
enQ(4)
enQ(5)
print(deq())
print(deq())
print(deq())
print(deq())
print(deq())