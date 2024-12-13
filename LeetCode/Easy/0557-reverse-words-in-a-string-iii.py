# 문제
# 주어진 문자열 s 에서 각 단어를 뒤집어서 반환
# 공백과 단어의 순서는 유지해야 함

# 풀이
# 공백을 기준으로 단어를 구하고
# 슬라이싱으로 뒤집은 후 공백으로 이어줌


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])