T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = input()
    # 0 ~ 9 까지 리스트 할당
    li = [0] * 10
    # input 값으로 num(문자로 받아온값)을 정수형으로 변환
    # 변환 후 num값에 포함된 값들에 +1 해주기
    for i in num:
        i = int(i)
        li[i] += 1
    # 최대값, 인덱스값 만들기
    max1 = 0
    idx = 0
    # 리스트의 길이만큼 순환
    for j in range(len(li)):
        # max1 값이 li[j]보다 작으면
        # 값 변경 후 인덱스 값 추가
        if max1 <= li[j]:
            max1 = li[j]
            idx = j

    print(f'#{tc} {idx} {max1}')