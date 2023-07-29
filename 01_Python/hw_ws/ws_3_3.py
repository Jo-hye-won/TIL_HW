from book import decrease_book


def rental_book(name, number):
    decrease_book(number)  # rental_book 함수 실행될 때
                    # decrease_book 호출
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)
