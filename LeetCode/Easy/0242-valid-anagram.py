# 문제
# 문자열 s 와 t 가 주어짐
# t 가 s 의 anagram 인지 여부를 반환
# anagram 이란 기존 문자를 정확히 한 번 사용하여 재배열해서 만들어진 다른 단어나 문장

# 풀이
# s 와 t 는 길이가 동일해야 함
# t 의 각 문자가 s 에 포함된다면 하나씩 제거, 없으면 바로 False를 반환

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = list(s)
        for c in t:
            if c not in s:
                return False
            else:
                s.remove(c)

        return True