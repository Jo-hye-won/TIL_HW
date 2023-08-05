############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_item_price(item_list):
    
    # # 여기에 코드를 작성하여 함수를 완성합니다.
    total = 0
    for item in item_list:
        total += item['price']* item['count']

    return total

        #
        # one_price = item_list[0]['price']
        # one_count = item_list[0]['count']
        # price_1 = one_price * one_count
        #
        # two_price = item_list[1]['price']
        # two_count = item_list[1]['count']
        # price_2 = two_price * two_count
        #
        # three_price = item_list[2]['price']
        # three_count = item_list[2]['count']
        # price_3 = three_price * three_count
        #
        #
        # prices = price_1 + price_2 + price_3
        #
        # return prices


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    SSAFANG_ITEM_LIST = [
        {
          'name': 'Galaxi Buds',
          'count': 3,
          'price': 150000,
        },
        {
          'name': 'Galaxi Pro Book 3',
          'count': 2,
          'price': 1500000,
        },
        {
          'name': 'Galaxi Mouse Pro',
          'count': 3,
          'price': 21000,
        },
    ]
    print(calc_item_price(SSAFANG_ITEM_LIST))  # => 3513000
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
