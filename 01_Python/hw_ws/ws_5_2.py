def remove_duplicates(lists):
    new_lst = []
    sett = set(lists)    # set으로 중복 없애고
    lists2 = list(sett)  # 리스트형식으로 변환한 후 
    # new_lst.append(lists2)    # new_lst에 담아주기
    new_lst.extend(lists2)
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(*result)  # 에스터리스크를 사용해서 리스트 안의 요소만 출력하기(언패킹)
print(result)