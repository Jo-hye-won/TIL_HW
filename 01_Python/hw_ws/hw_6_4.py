# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dict,di,di2):
    sets = dict
    dict[di] = di2
    sets.update(dict)
    return sets

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)

#     new_dict = dict.copy()
#     # new_dict = dict # 이케 그냥 할당해줘도 됨
#     new_dict.setdefault(di,di2)
 
#     # new_dict.setdefault(di,di2)

# #     # dictionary = {
# #     #     'name': dict['name'],
# #     #     'age': dict['age'],
# #     #     'country': sum_dict['country']
# #     # }
# #     # dict.setdefault('di','di1').items()
# #     # new_dict.setdefault(di,di1)
    
#     return new_dict
# def add_item_to_dict(dict,di,di2):
#     key, value = my_dict.items()
#     new_dict = {}
#     new_dict.update('key','value')
#     return new_dict
