# 문제
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
# 연산들이 문자열로 주어진 배열 operations 가 주어짐
# 모든 연산을 수행한 후 최종 x 의 값을 반환

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            elif '-' in op:
                x -= 1
        return x