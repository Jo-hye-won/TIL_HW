import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))



'''   
T = int(input())

# 테스트 케이스로 받아온 T 값 만큼 반복문 돌리기
for tc in range(1, T+1):
  # 며칠 받을지 값 n 정하기
  n = int(input())
  # 가격 리스트로 값 받기
  li = list(map(int, input().split()))
  # 최대 값 미리 변수 할당
  max_price = li[n-1]
  # 이익 변수 할당
  money = 0

  # 역순으로 마지막 전전 값부터 값을 찾기
  # n-2 부터 0 까지
  for i in range(n-2, -1, -1):
    # max_price 값 보다 리스트에 속해있는 값이 클경우
    # 최대값 변경해주기
      if li[i] > max_price:
          max_price = li[i]
    # 그게 아니면 이익에 값 넣어주기
      else:
          money += max_price - li[i]

  print(f"#{tc} {money}")
'''