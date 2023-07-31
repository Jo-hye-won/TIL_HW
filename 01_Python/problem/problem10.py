############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):

    # 여기에 코드를 작성하여 함수를 완성합니다.
   
    row_len = 0
    col_len = 0

    for row in matrix:
        row_len += 1
        for _ in row:
            col_len += 1
            break
    
    for row in range(row_len):
        for col in range(col_len):
            if matrix[row][col] == 1:
                return row, col



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
