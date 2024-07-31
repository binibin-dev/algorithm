# 문제
# 정수 배열 nums 와 정수 k 가 주어짐
# nums 에서 k 번째로 큰 값을 반환 (중복을 고려해야 함)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSort(arr, first, last):
            if first >= last: return arr
            p = arr[first]
            left, right = first + 1, last

            while left <= right:
                while left <= last and arr[left] < p:
                    left += 1
                while right >= first and arr[right] > p:
                    right -= 1
                if left <= right:
                    arr[left], arr[right] = arr[right], arr[left]
                    left += 1
                    right -= 1
            arr[first], arr[right] = arr[right], arr[first]
            quickSort(arr, first, right - 1)
            quickSort(arr, left, last)

            return arr

        return quickSort(nums, 0, len(nums) - 1)[-k]