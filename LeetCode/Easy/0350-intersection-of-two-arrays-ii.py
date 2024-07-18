# 문제
# 주어진 두 배열의 교집합을 구함
# Each element in the result must appear as many times as it shows in both arrays.

# 풀이
# intersection 의 최대 크기는 nums1 과 nums2 중 작은 배열의 크기일 것임
# 작은 배열에 있는 값들을 순회하면서 다른 배열에 해당 값이 포함되는지 확인
# 다른 배열에 포함된다면 해당 값을 result에 추가 후 삭제

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) <= len(nums2):
            for n in nums1:
                if n in nums2:
                    result.append(n)
                    nums2.remove(n)
        else:
            for n in nums2:
                if n in nums1:
                    result.append(n)
                    nums1.remove(n)
        return result