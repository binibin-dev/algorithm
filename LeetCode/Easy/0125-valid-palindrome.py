# 모든 문자를 소문자로 바꾸고 알파벳이나 숫자가 아닌 문자를 모두 지우면 회문인 s 가 주어줌

# isalnum() 은 문자열이 a-zA-Z1-9 로 이루어져 있는지를 반환함

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        if s == s[::-1]: # s[::-1] 는 s 를 뒤집은 결과
            return True
        return False