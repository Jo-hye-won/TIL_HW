import requests
from pprint import pprint as print
dummy_data = []
for i in range(1,11):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL)
    parsed_list = response.json()
    dummy_dict = {'company' : parsed_list['company']['name'] ,
                   'lat' : parsed_list['address']['geo']['lat'], 
                   'lng' : parsed_list['address']['geo']['lng'],
                   'name' : parsed_list['name']}
    if abs(float(parsed_list['address']['geo']['lat'])) < 80 and abs(float(parsed_list['address']['geo']['lng'])) < 80:
        dummy_data.append(dummy_dict)
print(dummy_data)

# import requests
# from pprint import pprint as print

# dummy_data = []
# for i in range(1,11):
#     tmp_dict = {}
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
#     response = requests.get(API_URL)
#     data = response.json()
#     name = data['name']
#     lat = float(data['address']['geo']['lat'])
#     lng = float(data['address']['geo']['lng'])
#     if -80 < lat < 80:
#         tmp_dict['lat'] = lat
#     if -80 < lng < 80:
#         tmp_dict['lng'] = lng

#     company_name = data['company']['name']
#     tmp_dict['company_name'] = company_name
#     tmp_dict['name'] =name
#     dummy_data.append(tmp_dict)


    
# import requests
# from pprint import pprint as print
# dummy_data = []
# dummy_dic = {}

# for i in range(1,11):
#     API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
#     response = requests.get(API_URL)
#     parsed_data = response.json()
#     dummy_data.append(parsed_data['name'])
#     dummy_data.append(parsed_data['address']['geo']['lat'])
#     dummy_data.append(parsed_data['address']['geo']['lng'])
#     dummy_data.append(parsed_data['company']['name'])

# print(dummy_data)   