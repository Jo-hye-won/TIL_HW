list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전',
                '만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전',
                '도문대작','옥루몽','옥련몽']

rental_book = ['장생전','위대한 개츠비', '원생몽유록','이생규장전', '데미안', 
               '장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']

missing_book = [i for i in rental_book if i not in list_of_book]

all_pass = True

for i in rental_book:
  if i not in list_of_book:
    print(f'{i} 을/를 보충하여야 합니다.')
    all_pass = False

if all_pass:
  print("모든 도서가 대여 가능한 상태입니다")

# print(missing_book)


# 보유중이지 않은 책 찾기
# list comprehension은 새로운 리스트 만들어서 변수에 할당하는 것이다. 
# missing_book 변수에 새로운 리스트가 할당 된 것!

# missing_book = []
# for rental in rental_book:
#     if rental not in list_of_book:
#         missing_book.append(rental)
# print(missing_book)

# missing_book = [rental for rental in rental_book if rental not in list_of_book]

# for missing in missing_book:
#     print(f'{missing}을 보충해야 합니다.')

# # 없는 책을 담기로 했던 missing_book 리스트가 비어있으면, 아래 문구를출력할 수 있다. 
# # 비어있는 리스트 [] == False
# # 값이 있는 리스트 -> if : True
# if missing_book:
#     pass
# else:
#     print('모든 도서가 대여 가능한 상태입니다.')

# if not missing_book :
#     print('모든 도서가 대여 가능한 상태입니다.')

# if missing_book == Flase:
#     print('모든 도서가 대여 가능한 상태입니다.')

# if missing_book == []:
#     print('모든 도서가 대여 가능한 상태입니다.')