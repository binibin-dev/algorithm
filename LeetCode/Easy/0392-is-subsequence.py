# 문제
# 문자열 s, t 가 주어짐
# s 가 t 의 subsequence 이면 True, 아니면 False 를 반환
# subsequence 란 기존 문자열에서 어떤 문자들을 삭제하여 얻을 수 있는 새로운 문자열
# 상대적인 위치는 유지되어야 함

# 풀이
# 반복할 때마다 무조건 t 의 인덱스는 하나씩 증가
# s 의 인덱스는 해당 요소가 t에 포함될 때만 증가
# 반복하다가 s 가 모두 발견되어 len(s) 와 같아지면 True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        return si == len(s)