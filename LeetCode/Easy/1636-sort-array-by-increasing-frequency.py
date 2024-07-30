# 문제
# 정수 배열 nums 가 주어짐
# 값의 빈도에 따라 오름차순으로 정렬
# 만약 빈도수가 동일한 값이 여러 개 있다면, 내림차순으로 정렬

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        def custom_sort(num):
            return (counter[num], -num)
        
        nums.sort(key=custom_sort)
        return nums