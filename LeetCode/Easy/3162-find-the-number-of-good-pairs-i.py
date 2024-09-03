# 문제
# 각각 길이가 n 과 m 인 정수 배열 nums1, nums2 가 주어짐
# 양의 정수 k 또한 주어짐
# nums1[i] 가 nums2[j]*k 로 나눠지는 (i, j) 쌍을 good pair 라고 함
# good pairs 의 개수를 반환

# 풀이
# nums1[i] // nums2[j]*k >= 1 이면서 nums1[i] % nums2[j]*k == 0 이라면 (i, j) 는 good pairs


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j]*k) == 0:
                    count += 1
        return count