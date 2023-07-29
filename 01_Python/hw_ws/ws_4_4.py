import requests
import pprint

# from pprint import pprint as print

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

dummy_list = []

for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dummy_data = {'company' : parsed_data['company']['name'] ,
                    'lat' : parsed_data['address']['geo']['lat'], 
                   'lng' : parsed_data['address']['geo']['lng'],
                   'name' : parsed_data['name']}
    if abs(float(parsed_data['address']['geo']['lat'])) < 80 and abs(float(parsed_data['address']['geo']['lng'])) < 80:
        dummy_list.append(dummy_data)

# pprint.pprint(dummy_list)
# ======================================================================
A = {}
def create_user(n):
    B = dummy_list[n]['company']
    C = dummy_list[n]['name']
    A[B] = C
    return A

for i in range(len(dummy_list)):
    create_user(i)

Company_name = list(A.keys())

censored_user_list = {}

def censorship():
    for i in Company_name:
        Name = A[f'{i}']
        if i in black_list:
            print(f'{i} 소속의 {Name} 은/는 등록할 수 없습니다.')
        else :
            print('이상 없습니다.')
            censored_user_list[f'{i}'] = [f'{Name}']

censorship()
pprint.pprint(censored_user_list)