# 문제
# 아이들에게 최대 1개의 쿠키를 나눠줘야 함.
# 각 아이 i는 만족할 수 있는 최소의 쿠키 사이즈를 나타내는 g[i] 가 있음
# 또한 각 쿠키 j 는 사이즈를 가지고 있음
# 만족하는 아이의 수를 최대화하고 그 최대 수를 출력

# 풀이
# greed factor 와 size 를 오름차순으로 정렬
# greed factor 의 요소마다 size 요소를 하나씩 비교
# g 가 s 보다 작으면 아이가 만족하기 때문에 해당 s 를 size 배열에서 삭제하고 횟수를 카운팅
# 이를 반복하면서 중간에 s가 하나도 남아 있지 않으면 return 해야 함

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        result = 0
        for i in g:
            if len(s) == 0:
                return result
            for j in s:
                if i <= j:
                    s.remove(j)
                    result += 1
                    break
        return result