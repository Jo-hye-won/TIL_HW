from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd



def read_csv_data(request):
    file_path = 'data/test_data_has_null.csv'
    
    df = pd.read_csv(file_path, encoding='cp949')
    data = df.to_dict('records')
    # print(df['나이'].mean())
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 


def B(request):
    file_path = 'data/test_data_has_null.csv'
    
    df = pd.read_csv(file_path, encoding='cp949')
    # df.head()
    # replace_null = data.fillna("NULL", inplace=True)
    df.fillna('NULL', inplace=True)
    print(df.isna().sum())
    data = df.to_dict('records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 
    # return JsonResponse({'data': replace_null})


file_path = 'data/test_data_has_null.csv'
df = pd.read_csv(file_path, encoding='cp949')
def C(request):
    global df
    average_age = df['나이'].dropna().mean() # 평균 나이 구해주기 
    # print(average_age)

    # 평균나이와의 차이 필드 생성해주기 
    df['평균 나이와의 차이'] = abs(df['나이'] - average_age)
    chai_df = df.nsmallest(10, '평균 나이와의 차이')
    data = chai_df.to_dict(orient='records')
    return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200) 

# @api_view(['GET'])
# def db_analysis(request):
#     df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')

#     tmp = df.fillna('NULL')
#     tmp['나이'] = pd.to_numeric(tmp['나이'], errors='coerce')
#     mean_age = tmp['나이'].mean()

#     sorted_df = tmp.dropna(subset=['나이'])
#     sorted_df['차이'] = abs(sorted_df['나이'] - mean_age)

#     sorted_df = sorted_df.sort_values(by='차이').head(10).drop('차이', axis=1)

#     new_df = sorted_df.to_dict('records')

#     return JsonResponse({'new_df': new_df }, json_dumps_params={'ensure_ascii': False}, status=200)
    

df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')
@api_view(['GET'])
def db_analysis(request):
    global df

    tmp = df.fillna('NULL')
    tmp['나이'] = pd.to_numeric(tmp['나이'], errors='coerce')
    mean_age = tmp['나이'].dropna().mean()
    tmp['차이'] = abs(tmp['나이'] - mean_age)

    sorted_df = tmp.sort_values(by='차이').head(10).drop('차이', axis=1)
    sorted_df = sorted_df.to_dict('records')

    return JsonResponse({'data': sorted_df }, json_dumps_params={'ensure_ascii': False}, status=200)


array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)
