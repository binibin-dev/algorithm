# 문제
# 주어진 문자열에서 가장 먼저 나오는 유일한 문자의 인덱스를 반환
# 없으면 -1 을 반환


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1

        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1