############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    # ls = word.split() -> 공백없으니까 ㄴㄴ
    # return type(a)
    # 여기에 코드를 작성하여 함수를 완성합니다.
    lss = []
    lis = list(word)
    for i in range(12):
        # return i
        if lis[i].isdigit():
            lss.append(i)
        return lss
    
    # return lss
        # for j in range(len(lss)):
        #     if str(lss[j]).isdigit():
        #         return str(lss[j])
        


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    