# 숫자 카드

import sys
sys.stdin = open('card.txt')


T = int(input())       # 테스트 케이스 개수

for tc in range(1, T+1):
  N = int(input())       # 카드 장수
  card = list(map(int, list(str(input())))) # 카드들 한장씩빼서 리스트로
  # print(card)
  # card = list(map(int, input()))


tmp = [0] * 10 # 카드의 개수만큼 0을 채운 리스트 생성
for c in range(N):
  tmp[card[c]] += 1

count = 0
for i in range(len(card)):
  if count <= card[i]:
    count = card[i]
    tmp = i


#
#
# #
print(f'#{T+1} {tmp} {count}')
#
# # input 텍스트를 불러오기 위한 코드.
# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
# # 테스트케이스 갯수
# T = int(input())
#
# for test_case in range(1, T + 1):
#   # N개의 숫자카드가 주어진다.
#   N = int(input())
#   # 처음 들어오는 input타입이 string이므로 int로 변환해서 list에 넣기
#   arr = list(map(int, input()))
#
#   # 카드의 최대값의 초기값 설정.
#   max_card = arr[0]
#   # 리스트를 돌면서 최대값을 가진 카드 찾기.
#   # 카운팅 할 배열을 만들기 위해서 최대값 카드 찾기.
#   for m in arr
#     if m > max_card:
#       max_card = m
#
#   # 카운팅을 넣을 빈 배열만들기(최댓값의 +1의 길이로)
#   count_list = [0] * (max_card + 1)
#   # 순회하면서 각 카드의 숫자별로 갯수 카운팅하기
#   for i in range(0, N):
#     # i의 값만큼 count_list의 인덱스로 가서 1씩 더해주기
#     count_list[arr[i]] += 1
#     # 출력을 위한 초기값 설정
#     max_count = 0
#     temp_card = 0
#     # 정렬된 count_list를 돌면서
#     for j in range(0, len(count_list)):
#       # count_list의 값의 최대를 찾아
#       # 여기서 **크거나 같다**를 설정해 준 이유는 카드의 장수가 같더라도 더 값이 큰 카드를 출력하기 위해서!
#       if count_list[j] >= max_count:
#         # 최대값을 저장하고
#         max_count = count_list[j]
#         # 그 최대값을 가지는 인덱스값이 즉 카드숫자!
#         temp_card = j
#
#   print('#{} {} {}'.format(test_case, temp_card, max_count))