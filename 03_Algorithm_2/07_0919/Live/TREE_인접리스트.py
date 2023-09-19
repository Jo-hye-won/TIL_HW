arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
#  이진 트리 만들기
nodes = [[] for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

# 자식이 더 이상 없다는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return

    preorder(nodes[nodeNumber][0])
    preorder(nodes[nodeNumber][1])
    print(nodeNumber, end=' ')

preorder(1)