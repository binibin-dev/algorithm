# 문제
# 정수 nums 가 주어짐
# 0 까지 감소 시키는 step 의 횟수를 반환
# 한 번의 step 에서는 현재 숫자가 짝수면 2로 나눈 수, 아니라면 1을 뺀 수로 업데이트


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count +=1
        return count