# 문제
# 정수 배열 nums 와 정수 k 가 주어짐
# 서로 다른 i 와 j에 대해 해당 인덱스의 값이 같고 둘의 차이가 k보다 작거나 같다면 True 를 반환

# 풀이
# 키로 nums 에 있는 요소, 값으로 nums에서의 인덱스 쌍을 저장하기 위해 빈 딕셔너리를 생성
# nums 크기만큼 반복하며 딕셔너리의 키로 현재 인덱스(i)의 값(nums[i])이 있는지 확인
# 있다면 현재 인덱스 i와 해당 키의 값(d[nums[i]], 즉 인덱스)의 차를 구하여 k 보다 작거나 같으면 True 반환
# 없다면 딕셔너리에 nums[i]: i 를 추가

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False