# ws_5_5.py

# # 아래 함수를 수정하시오.
# def even_elements(lists):
#     ghftn = []
    
#     for odd in my_list:
#         if int(odd) == 1:
#             ghftn.append(lists.pop(odd))
#         else:
#             continue

#     return ghftn

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)

def even_elements(li):
    wkrtn = []   # 짝수넣을 리스트만들기
    while True:
        if len(li) == 0:  # 종료조건
            break

        num = li.pop()  # 끝에서 하나씩 빼서
        
        if num % 2 == 0:    # 짝수인지 확인해보자
            wkrtn.extend([num])  # 짝수면 담기렴
            # wkrtn.extend(num)
        wkrtn.sort()  # 정렬하자
        # b = sorted(wkrtn) # sorted쓰려면 변수할당 해주고 return값을 b로 해줘야함
    return wkrtn       # 반환!!

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)

# def even_elements(num_list):
#     i = 0
#     while i < len(num_list):
#         if num_list[i] % 2 != 0:  # 홀수면 빼내자!
#             num_list.pop(i)
#         else:
#             i += 1                # 홀수 아니면 인덱스 +1해주자
#     return num_list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = even_elements(my_list)
# print(result)
