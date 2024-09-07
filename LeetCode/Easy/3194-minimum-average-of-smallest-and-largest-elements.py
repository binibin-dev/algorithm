# 문제
# 부동소수점 수 인 averages 의 배열을 가졌다고 가정 (빈 배열로 초기화된 상태)
# 짝수(n)개의 정수로 이뤄진 nums 가 주어짐
# 아래의 과정을 n/2 번 반복
# - nums 에서 가장 작은 요소 minElement 를 제거 후 가장 큰 요소 maxElement 를 제거
# - averages 에 (minElement + maxElement) / 2 를 더함
# averages 에서 가장 작은 요소를 반환

# 풀이
# 제거한 값을 활용해야 하므로 pop 메서드 사용
# 가장 작은 값과 가장 큰 값을 선택하는 과정이 반복되므로 정렬된 상태에서 시작


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        while nums:
            minval = nums.pop(0)
            maxval = nums.pop(-1)
            averages.append((minval + maxval) / 2)
        return min(averages)