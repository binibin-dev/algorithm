# 문제
# 보석인 돌들의 종류를 나타내는 문자열 jewels 과 가지고 있는 돌들을 나타내는 문자열 stones 가 주어짐
# stones 의 각 문자는 가지고 있는 돌의 종류임
# 가지고 있는 돌들 중 몇 개가 보석인지 반환
# 대소문자를 구분함

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([s in jewels for s in stones])