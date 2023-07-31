############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
   
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    counter = 0
    total  = 0
    for speed in speed_list:
        total += speed
        counter += 1

    avg = total / counter
    return avg


    #     if speed_list[i] > 100:

    # a = speed_list[0]
    # b = speed_list[1]
    # c = speed_list[2]
    # d = speed_list[3]
    # sums = a + b+ c + d
    # avg = sums / 4

    # return float(avg)

    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    

    # for speed in speed_list:
    #     # return speed
    #     counter.append(speed)
    #     return counter
    #     # if int(speed) > 100:
        #     # counter.append(speed)
        #     counter = counter + speed
        #     return counter
        #     # counter_sum = int(counter[0] + counter[1] + counter[2] + counter[3]) //4
        # #     for i in range(len(counter)):
        # #         counter_sum = (counter[i])

        # else:
        #     continue
    # return counter_sum