# 문제
# 양의 정수인 low 와 high 가 주어짐
# x 는 2*n 자리로 구성, 첫 번째 n 자리의 합이 마지막 n 자리의 합과 같을 경우 symmetric(대칭)이며, 이 대칭의 개수를 출력
# odd number of digits 즉 홀수자리는 대칭이 될 수 없음

# 풀이
# low와 high 사이에 있는 정수들을 구함
# 홀수자리가 아니면서 첫 번째 n 자리의 합이 마지막 n 자리의 합과 같은지 비교

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for i in range(low, high+1):
            s = str(i)
            if len(s) == 2:
                if s[0] == s[1]:
                    result += 1
            elif len(s) == 4:
                if int(s[0]) + int(s[1]) == int(s[2]) + int(s[3]):
                    result += 1
        
        return result
