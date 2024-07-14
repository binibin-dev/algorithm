# 문제
# 정수 x가 palindrome(회문) 인지 아닌지를 반환

# 풀이
# 회문은 i번째와 뒤에서 i번째 값이 같아야 함
# 수의 길이가 짝수면 절반 나눠서 확인
# 수의 길이가 홀수면 가운데는 어떤 수여도 상관 없기 때문에 가운데를 제외하고 나머지만 확인

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = str(x)
        test = len(string) // 2
        
        for i in range(test):
            if string[i] != string[-(i+1)]:
                return False
        return True
