# 문제
# 문자열 s 와 t 가 주어짐
# t 가 s 의 anagram 인지 여부를 반환
# anagram 이란 기존 문자를 정확히 한 번 사용하여 재배열해서 만들어진 다른 단어나 문장

# 풀이
# 두 문자열을 순서대로 정렬한 값이 같으면 anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)