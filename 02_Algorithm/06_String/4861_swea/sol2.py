import sys
sys.stdin = open('input.txt')

T = int(input())  # 테스트 케이스 3개

for tc in range(1, T+1):   # 3번 순회하면서
    N,M = map(int, input().split())    # 10 10
    alpas = [input() for _ in range(N)]

    '''print(alpas)
    ['GOFFAKWFSM', 'OYECRSLDLQ', 'UJAJQVSYYC', 'JAEZNNZEAJ', 'WJAKCGSGCF', 'QKUDGATDQL', 'OKGPFPYRKQ', 'TDCXBMQTIO',
     'UNADRPNETZ', 'ZATWDEKDQF']
    ['WPMACSIBIK', 'STWASDCOBQ', 'AMOUENCSOG', 'XTIIGBLRCZ', 'WXVSWXYYVU', 'CJVAHRZZEM', 'NDIEBIIMTX', 'UOOGPQCBIW',
     'OWWATKUEUY', 'FTMERSSANL']
    ['ECFQBKSYBBOSZQSFBXKI', 'VBOAIDLYEXYMNGLLIOPP', 'AIZMTVJBZAWSJEIGAKWB', 'CABLQKMRFNBINNZSOGNT',
     'NQLMHYUMBOCSZWIOBINM', 'QJZQPSOMNQELBPLVXNRN', 'RHMDWPBHDAMWROUFTPYH', 'FNERUGIFZNLJSSATGFHF',
     'TUIAXPMHFKDLQLNYQBPW', 'OPIRADJURRDLTDKZGOGA', 'JHYXHBQTLMMHOOOHMMLT', 'XXCNJGTXXKUCVOUYNXZR',
     'RMWTQQFHZUIGCJBASNOX', 'CVODFKWMJSGMFTCSLLWO', 'EJISQCXLNQHEIXXZSGKG', 'KGVFJLNNBTVXJLFXPOZA',
     'YUNDJDSSOPRVSLLHGKGZ', 'OZVTWRYWRFIAIPEYRFFG', 'ERAPUWPSHHKSWCTBAPXR', 'FIKQJTQDYLGMMWMEGRUZ']
'''
    cnt = 0     # 길이 구할 변수 초기화
    # ls =[]  # 회문 넣을 리스트
    for i in range(N):  # 배열 크기 10만큼 순회하면서
        for j in range(N-M+1):  # N*N 크기의 글자판이긴 하지만 길이가 M인 회문을 찾아야하니까
                                # 그냥 N하면 범위오류날거다
            # 가로 탐색
            for k in range(M//2):  # 절반만 확인하면 되기 때문에 //2
                if alpas[i][j+k] != alpas[i][j+M-1-k]:  # alpas의 [0][0]= G랑
                                                        # alpas의[0][9]=M을 비교해서 동일하지 않으면
                    break  # 멈춘다~!
            else:   # 같은 경우에는
                print(alpas[i][j:j+M])

            # 세로 탐색
            for l in range(M//2):
                if alpas[j+l][i] != alpas[j+M-1-l][i]:
                    break
            else:
                # print(alpas[i:i+M][j])
                # print(alpas[j:j + M][i])
                print(alpas[])