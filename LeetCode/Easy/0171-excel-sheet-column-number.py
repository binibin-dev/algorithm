# 문제
# 컬럼 이름을 나타내는 문자를 정수로 반환
# A 는 1, B는 2, ..., AA 는 27, AB 는 28
# 예시로 미루어 보았을 때 BA 는 26**(2-1) + 1

# 풀이
# A 는 유니코드로 65이며 이 문제와 64가 차이남
# 한 자리가 늘어갈수록 26을 문자에 해당하는 수만큼 곱함 (거듭제곱)
# 문자열을 뒤집고 각 문자의 ord(문자) - 64 + 26**(자릿수)를 게산한 결과를 모두 합침

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, c in enumerate(reversed(columnTitle)):
            result += (ord(c)-64) * 26**i
        return result