# 16진법으로 바꾸기 위한 dict
diction16 = {
    0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
    6:'6', 7:'7', 8:'8', 9:'9', 10:'A',
    11:'B', 12:'C', 13:'D', 14:'E', 15:'F'
}

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # H와 P의 자릿수
    H = input()             # H, key 를 ^ 연산하여 P를 만들 것
    key = input()
    final = ''              # 계산 결과
    # print(H)
    # print(type(H))

    # ^연산을 통해 H의 모든 원소와 진행하면서 결과를 더해가기
    for i in H:
        mid = int(i, base=16) ^ int(key, base=16)
        # print(mid)
        # print(diction16[mid])
        final += diction16[mid]

    print(f'#{tc}', final)