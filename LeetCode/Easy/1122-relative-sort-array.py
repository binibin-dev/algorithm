# 문제
# 배열 arr2 에 있는 요소는 서로 다르고, arr2 에 있는 모든 요소는 arr1 에도 존재함
# arr2 와 동일하게 arr1 의 상대적인 순서를 정렬해야 함
# arr2 에 없는 요소는 arr1의 끝에 오름차순으로 정렬되어야 함

# 풀이
# sort 메서드의 키로 전달할 함수를 만들어야 함
# 참고로 arr2 에 있는 숫자가 앞에 나와야 하며, 그 순서는 arr2 의 순서와 동일해야 함
# 또한 arr2 에 없는 숫자는 arr2 에 있는 숫자가 모두 정렬된 후 그 뒤에 오름차순으로 정렬되어야 함
# 따라서 arr2 에 있는 숫자일 경우 (0, index_map[num]) 을 반환
# arr2 에 없는 숫자일 경우 (1, num) 을 반환

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_map = {v: i for i, v in enumerate(arr2)}

        # define a custom sorting function (sort 의 키로 전달할 함수)
        def custom_sort(num): # num 은 sort 할 배열의 요소 하나를 의미
            if num in index_map: # arr1 의 요소가 d에 있는 경우
                return (0, index_map[num])
            else:
                return (1, num)
        
        arr1.sort(key=custom_sort)
        return arr1
                