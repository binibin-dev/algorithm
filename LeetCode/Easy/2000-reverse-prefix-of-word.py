# 문제
# 문자열 word 와 문자 ch 가 주어짐
# word 에서 인덱스 0부터 ch 가 처음으로 발생하는 인덱스 사이에 있는 문자열 부분을 뒤집어서 반환
# (기존 문자열에서 위의 부분만 뒤집어서 반환)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        last = word.index(ch)
        return ''.join(reversed(word[:last+1])) + word[last+1:]