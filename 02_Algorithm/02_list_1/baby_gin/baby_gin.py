import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range (1,T+1):
    num = int(input())
    tmp = [0] * 12     # 0부터 9까지 +

    for i in range(6):
        tmp[num % 10] += 1  # num의 마지막 일의자리 숫자를 인덱스로 활용해서
                      # 그 자리에 +1 해줌

        num //= 10  # num을 10으로 나눈 몫을 다시 num에 할당
                # num의 일의 자리가 제거되고,십의 자리가 일의 자리로 이동!!

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:   #triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")

