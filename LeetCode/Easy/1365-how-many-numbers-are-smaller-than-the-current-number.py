# 문제
# 배열 nums 가 주어짐
# nums 에서 각 nums[i] 보다 작은 수가 몇 개 있는지 반환

# 풀이
# 효율적인 연산을 위해 nums 를 정렬해야 함
# 중복되지 않은 nums 의 요소를 키로,
# 해당 키가 중복되지 않은 nums 중 몇 번째인지를 값으로 가지는 딕셔너리 생성
# 위에서 생성한 딕셔너리의 값들은 키보다 작은 값이 몇 개 있는지를 나타냄


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(sorted(nums)):
            if n not in d:
                d[n] = i
        answer = [d[n] for n in nums]
        return answer