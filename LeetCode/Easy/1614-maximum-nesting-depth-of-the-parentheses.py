# 문제
# 괄호 문자열 s 가 주어짐
# s 의 중첩된 깊이를 반환 (중첩된 깊이 = 중첩된 괄호의 최대 개수)

# 문제
# 중첩된 깊이를 나타내는 변수 ndepth 를 0으로 초기화
# 열린 괄호라면 스택에 삽입
# 닫힌 괄호라면 스택에서 삭제
# 스택에 요소가 삽입될 때마다 스택에 있는 요소의 총 개수를 ndepth 와 비교하여 큰 값으로 업데이트


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ndepth = 0

        for c in s:
            if c == '(':
                stack.append(c)
                ndepth = max(len(stack), ndepth)
            elif c == ')':
                stack.pop()
        
        return ndepth