# 문제
# 정수 n 이 주어짐
# ans[i] 가 i 의 이진 표현에서의 1의 개수인 길이가 n + 1 인 배열을 반환

# 풀이
# 0부터 n까지 반복
# 각 숫자를 이진 표현으로 변환 후 1의 개수를 셈


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            element = sum([True if d=='1' else False for d in bin(i)[2:]])
            result.append(element)
        return result