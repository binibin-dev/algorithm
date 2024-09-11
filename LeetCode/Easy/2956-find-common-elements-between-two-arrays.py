# 문제
# 크기가 n 과 m 인 두 정수 배열 nums1 과 nums2 가 주어짐
# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# [answer1, answer2] 를 반환


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1, a2 = 0, 0
        
        for n1 in nums1:
            if n1 in nums2:
                a1 += 1

        for n2 in nums2:
            if n2 in nums1:
                a2 += 1
        
        return [a1, a2]