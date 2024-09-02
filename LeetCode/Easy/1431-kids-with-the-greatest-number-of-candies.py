# 문제
# 정수 배열 candies 와 여분의 사탕의 개수를 나타내는 extraCandies 가 주어짐
# candies[i] 는 i 번째 아이가 가지고 있는 사탕의 수
# 길이가 n 인 boolean 배열을 반환
# i 번째 아이에게 여분의 사탕을 모두 줬을 때 아이들 중 가장 사탕을 많이 가진 상태가 되면 true, 아니면 false


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        return result