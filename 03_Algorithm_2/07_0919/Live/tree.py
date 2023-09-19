
# 0. 이진트리 저장
#   - 일차원 배열 저장
# 1. 인접 리스트로 저장
# 2. 연결 리스트로 저장 - 개발용

# 연결 리스트로 해보자
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 삽입 함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return
        #  오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        return

    # 순회
    def preorder(self):
        # 아무것도 없는 트리를 조회할 때
        if self != None:
            # 전위
            # print(self.value, end=' ')
            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 중위
            # print(self.value, end=' ')
            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()
            # 후위
            print(self.value, end=' ')


arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
#  이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()

