# 문제
# 문장이란 선후행 공백 없이 하나의 공백에 의해 구분되는 단어들의 나열
# 각 단어는 영어 대소문자로 구성됨
# 각 단어 뒤에 1부터 시작하는 인덱스를 추가하여 문장에서 단어들을 재배열하여 문장을 섞을 수 있음
# "This is a sentence" can be shuffled as "sentence4 a3 is2 This1"
# 9개 이하의 단어가 섞인 문장 s가 주어짐
# 재구성하여 기존 문장을 반환

# 풀이
# 공백으로 단어들을 분리
# 각 단어의 마지막 문자(인덱스)를 기준으로 정렬 (sort 의 key 함수 지정)
# 각 단어의 마지막 문자를 제외한 단어들을 공백으로 이어 문장으로 재구성


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        words.sort(key=lambda word: word[-1])
        return ' '.join([word[:-1] for word in words])