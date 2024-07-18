# 문제
# 문자열 s 와 t 가 주어짐
# t 는 s 에 있는 문자를 섞고 하나의 문자를 임의의 위치에 추가해 만들어진 문자열
# 추가된 t 를 반환해야 함

# 풀이
# t 가 s 보다 길이가 긺
# 따라서 t 에서 s 를 빼면 추가된 문자가 나옴

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = list(t)
        for c in s:
            result.remove(c)
        return result[0]