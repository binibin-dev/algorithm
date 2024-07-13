# 문제
# haystack 에서 needle 이 처음 발생하는 인덱스를 반환
# haystack 에 needle 이 없다면 -1을 반환

# 풀이
# haystack 의 첫 글자부터 needle의 글자수만큼 비교
# 인덱스가 넘어가지 않도록 함

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0

        len_needle = len(needle)
        for i in range(len(haystack)-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1