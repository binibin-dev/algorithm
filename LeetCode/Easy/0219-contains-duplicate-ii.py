# 문제
# 정수 배열 nums 와 정수 k 가 주어짐
# 서로 다른 i 와 j에 대해 해당 인덱스의 값이 같고 둘의 차이가 k보다 작거나 같다면 True 를 반환

# 풀이
# 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
        return False