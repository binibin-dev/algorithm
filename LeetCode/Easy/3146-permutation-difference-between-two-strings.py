# 문제
# s 에 있는 문자가 최대 한번 등장하고 t 는 s 의 순열임
# permutation difference 는 각 문자열에 있는 문자들의 인덱스 간 절대차의 합으로 정의
# t 와 s 의 permutation difference 를 반환

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pd = 0
        for i in range(len(s)):
            pd += abs(i - t.index(s[i]))
        return pd