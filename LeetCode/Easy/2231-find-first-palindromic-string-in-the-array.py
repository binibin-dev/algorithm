# 문제
# 문자열 배열 words 가 주어짐
# 배열에서 첫 번째 회문 문자열을 반환


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""