import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    move = int(input())
    boxes = list(map(int, input().split())) # 박스별 높이를 담은 리스트
    cnt_arr = [0] * 101 # 0~100 까지 카운트(최대 상자 높이)
    box_arr = [0] * 100 # 가로의 길이(len(boxes))는 항상 100

    for i in range(100):
        cnt_arr[boxes[i]] += 1

    for i in range(1,101):
        cnt_arr[i] += cnt_arr[i-1]

    for box in boxes:
        cnt_arr[box] -= 1
        box_arr[cnt_arr[box]] =box

    print('카운트배열', cnt_arr)
    print('정렬결과', box_arr)
    # cnt_arr[i] == box_arr에서 i가 시작되는 index 값

    # max_box, min_box =