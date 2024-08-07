# 문제
# 문자열 s 가 주어짐
# 인접한(다음) 문자의 아스키 값과의 절대차들의 합을 반환

class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            sum += abs(ord(s[i]) - ord(s[i+1]))
        return sum