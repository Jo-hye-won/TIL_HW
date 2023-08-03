import sys
sys.stdin = open('input.txt')

def binary_search(arr, P, key):
    '''
    1~100까지 담겨있는 리스트, 전체쪽수, 찾아야 할 쪽번호를 변수로 설정함
    '''
    start = 0   # 인덱스 번호 0부터 시작
    end = P-1   # 전체 쪽수가 P니까 인덱스 번호의 마지막 = P-1다.

    count = 0   # 몇번만에 찾아지는지 세기 위해서 초기값 설정
    while start <= end:   # 시작점이 끝값보다 작으면 끝난다.
        mid = int((start + end)/2)   # 중간값은 이렇게 구하라고 문제에서 주어짐
        if arr[mid] == key:  # 리스트에서 mid 위치의 값이 찾아야 할 값과 같으면
            count += 1      # 마지막으로 count 한번 더해주고
            return count       # count 출력
        elif arr[mid] > key:    # 찾아야 할 값보다 크면, 오른쪽 버리고, 왼쪽 검색해야하니까
            end = mid       # 끝인덱스을 mid 로 설정해주기
            count += 1      # 그리고 아직 못찾았으니까 찾는 횟수 추가해주기
        else:               # 찾아야 할 값보다 작으면, 왼쪽 버리고, 오른쪽 검색해야 하니까
            start = mid     # 시작인덱스를 mid 로 설정해주기
            count += 1      # 그리고 아직 못찾았으니까 찾는 횟수 추가해주기


T = int(input())    # 테스트 케이스 개수
for i in range(1, T+1):     # 테스트 케이스 만큼 반복할거야
    # 전체 쪽수 = P
    # A가 찾을 쪽 번호 = pa
    # B가 찾을 쪽 번호 = pb
    P, pa, pb = map(int, input().split()) # 각 인자 받아오기
    # print(P, pa, pb)
    # numbers = [i for i in range(1, P+1)]  # 1-400까지 쪽수가 들어가 있을 리스트 만들기_2
    numbers = list(range(1, P+1))    # 1-400까지 쪽수가 들어가 있을 리스트 만들기
    # N = len(numbers)    # 전체쪽수로 사용될 길이를 구해도 되고 그냥 전체쪽수로 받아온 P 써도 됨
    PA = binary_search(numbers, P, pa)   # A의 경우 찾기 위한 함수 호출
    PB = binary_search(numbers, P, pb)   # B의 경우 찾기 위한 함수 호출

    if PA > PB:         # PA의 결과로 나온 count 개수가 PB의 count 개수보다 크면 더 많은 횟수가 필요했다는 거라서
        print(f'#{i} B')        # B가 이긴거!
    elif PA < PB:     # PA의 결과로 나온 count 개수가 PB의 count 개수보다 작으면 더 적은 횟수가 필요했다는 거라서
        print(f'#{i} A')    # A가 이긴거!
    else:              # 비겼을 경우
        print(f'#{i} 0')    # 0을 출력해라
