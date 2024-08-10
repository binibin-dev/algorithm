# 문제
# 2n 개의 요소를 가지는 nusm 가 주어짐
# 요소는 [x1, x2, ..., xn, y1, y2, ..., yn] 형태임
# 배열을 [x1,y1,x2,y2,...,xn,yn] 형태로 반환

# 풀이
# xn 의 인덱스가 i 라면, yn 의 인덱스는 i + n

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.extend([nums[i], nums[i+n]])
        return result