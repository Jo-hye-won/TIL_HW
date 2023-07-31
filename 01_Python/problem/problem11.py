############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # max = matrix[3][0] + matrix[3][1] + matrix[3][2]+matrix[3][3]
    # return max


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    def get_row_col_maxsum(matrix):
    row_len = 0
    col_len = 0
    MAX = 0
    direct = 'row'
    for _ in matrix[0]:
        col_len += 1
    for _ in matrix:
        row_len += 1

    for row in matrix:
        total = 0
        for col_val in row:
            total += col_val
        
        if MAX < total:
            MAX = total
    
    # 세로 합 구하기
    for c_idx in range(col_len):
        total = 0
        for r_idx in range(row_len):
            total += matrix[r_idx][c_idx]
        
        # 큰 값인지 확인
        if MAX < total:
            MAX = total
            direct = 'col'

    return direct, MAX