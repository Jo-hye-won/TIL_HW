islogined = True

# 전처리, 후처리 로직이 너무 길다!
# 중복되는 코드가 너무 많이 발생 ! -> 이걸 어떻게 없앨까?
# 파이썬의 데코레이터를 활용한다!

# myfunc : 핵심 로직을 구현한 함수 
def myFunc():
    # 로그인 되어있는지 여부를 확인
    print('myfunc')

    # 로직이 끝났다! 안내문

def my_decorator(func): # 본인이 감싸고싶은 함수를 파라미터로 받고
    def wrapper():
        # 전처리
        if not islogined:
            print('로그인 하고 와라!')
            return
        
        func()
        # 후처리
        print('로직 끝남!')
    return wrapper

@my_decorator
def myFunc():
    print('myfunc')

myFunc()
