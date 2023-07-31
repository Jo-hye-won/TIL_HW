############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_ls = []
    for n in range(number):
        if n % 2 == 1:
            n +=1
            
            sum_ls.append(n)
            return sum_ls
        
        
        # sums = 0
        # if (n // 2) != 0:
        #     if (n // 3) == 1:
        #         sums = sums + n
        #     return sums

## 오늘 시험 : 10 -> 11-> 7 순으로 중요함!!

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(sum_primes(22)) # => 60
    print(sum_primes(33)) # => 143
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    def sum_primes(number):
    result = 0
    for num in range(2, number):
        # is ~~
        # falg 변수
        is_prime = True

        #가지치기, 방어코드
        if num == 17:
            continue

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            result += num


    return result
