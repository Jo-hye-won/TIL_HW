############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def change_pwd(word, secret_code):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # ssafy 문자열의 각 자리의 문자가 secret_code의 key값과 같은 값을 반환시켜야 함
    # ls = list(word)
    # return ls
    # for i in range
    # # return secret_code['s']
    # for i in ls:
    #     return secret_code['i']
    
    #     if str(i) == secret_code['i']:

    #         return secret_code['i']
    a  = str(secret_code['s'])
    b  = str(secret_code['s'])
    c  = str(secret_code['a'])
    d  = str(secret_code['f'])
    e  = str(secret_code['y'])

    words = f'{a}{b}{c}{d}{e}'
    return words



# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    secret_code = {
        'a': 3,    'b': 8,    'c': 0,    'd': 1,
        'e': 7,    'f': 6,    'g': 7,    'h': 1,
        'i': 2,    'j': 5,    'k': 3,    'l': 6,
        'm': 5,    'n': 0,    'o': 7,    'p': 9,
        'q': 8,    'r': 2,    's': 4,    't': 9,
        'u': 6,    'v': 3,    'w': 2,    'x': 4,
        'y': 8,    'z': 1,    ' ': 0,
    }
    print(change_pwd('ssafy', secret_code)) # => 44368
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.


    # for st in list(word.split()):   
    #     # return st     # ssafy
    #     for key in secret_code:
    #         if st == key:
    #             values = secret_code[key]
    #             return values
            
    