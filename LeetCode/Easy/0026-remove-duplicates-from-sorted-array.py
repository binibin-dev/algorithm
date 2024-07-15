# 문제
# 오름차순으로 정렬된 nums 가 주어짐
# 각 요소는 중복되지 않도록 nums 자체를 변환하고 유일한 값의 개수를 반환
# 중복이 제거된 요소들의 순서는 기존과 동일해야 함

# 풀이
# set 타입으로 변환하면 순서가 바뀌므로 다시 정렬해야 함!
# 주어진 배열 자체를 중복이 없도록 바꾸고 개수를 반환해야 함을 유의

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums)) # nums 자체에서 중복 제거
        return len(nums) # 유일한 값의 개수 반환