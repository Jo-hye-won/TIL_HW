import sys
sys.stdin = open('input.txt')

'''
마디의 길이를 출력해라
패턴에서 반복되는 부분을 마디라고 부른다. 
'''

T = int(input())
cnt = 0 # 마디의 길이를 출력할거다

for tc in range(1, T+1):
    sentence = list(input())
    # print(sentence)
    N = len(sentence)
    # for i in range(N):
        # while sentence[i] ==