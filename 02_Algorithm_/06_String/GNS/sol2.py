target = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    num, lst = input().split()
    str_list = list(map(str, input().split()))
    length = int(lst)

    result = []

    for i in range(10):
        cnt = 0
        for STR in str_list:
            if STR == target[i]:
                cnt += 1

        result += [target[i]] * cnt

    print(num)
    print(*result)
    # print(f'{num}\n',*result)
# print('hello,\n world!')