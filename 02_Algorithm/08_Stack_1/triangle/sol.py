T = int(input())

for tc in range(1, T+1):
    N = int(input())
                                                # ls = []
                                                # for i in range(1, 5):
                                                #     arr = [1] * i
                                                #     ls.append(arr)
                                                # print(ls)
    arr = [[1]*x for x in range(1, N+1)]
    for i in range(1,len(arr)):
        for j in range(1,len(arr[i])-1):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    print(f'#{tc}')
    for k in arr:
        print(*k)

'''
[[1], arr[0][0] = 1
[1, 1], arr[1][0] = 1 
[1, 1, 1], 
[1, 1, 1, 1]]

arr[1][0] + arr[1][1] = arr[2][1]
arr[2][0] + arr[2][1] = arr[3][1]
arr[2][1] + arr[2][2] = arr[3][2]

'''