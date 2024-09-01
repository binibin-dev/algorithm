# 문제
# n 명의 직원이 있음
# i 번째 직원의 일하는 시간은 hours[i]
# 회사는 적어도 target 시간만큼은 직원들이 일하기를 요구함
# 위의 요구사항을 만족하는 직원의 수를 반환


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        number = 0
        for h in hours:
            if h >= target:
                number += 1
        return number