# 문제
# 오름차순으로 정렬된 정수 배열 nums1, nums2 와 각각의 요소 개수 m, n 이 주어짐
# 두 배열을 오름차순으로 정렬하여 하나의 리스트로 병합해야 함
# 결과 리스트는 return 하지 않고 기존의 nums1 에 저장해야 함
# nums1 의 길이는 m+n 이며 앞에 m 개의 요소가 병합해야 하는 요소임

# 풀이
# nums1 의 앞 m 개와 nums2를 합쳐 정렬

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m] + nums2
        nums1[:] = sorted(nums1)