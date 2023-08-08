# 4865
import sys
sys.stdin = open('input.txt')

# 딕셔너리 이용?
# str1의 글자들이 str2에 몇개씩 들어있는지.
# str1의 글자의 종류들을 뽑아내서, str2와 대조.

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    words_dic = {}    # str1 단어들 딕셔너리로 만들기
    for word in str1:
        word_dic = {word : 0}   # 같은 단어 찾을 때마다 1씩 채워나갈 것.
        words_dic.update(word_dic)

    for word in words_dic: # words 딕셔너리 key를 순회하면서
        for char in str2: # str2를 순회하면서
            if char == word: # 둘이 일치하면
                words_dic[word] += 1 # 해당 딕셔너리 밸류에 +1

    max_word = 0 # 최댓값을 뽑기 위한 변수 설정
    for value in words_dic.values(): # 딕셔너리의 밸류 중에서
        if max_word < value:
            max_word = value # 최댓값 뽑기

    print(f'#{tc} {max_word}')