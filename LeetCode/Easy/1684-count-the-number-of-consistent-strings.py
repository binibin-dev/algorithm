# 문제
# 별개의 문자들로 구성된 문자열 allowed 와 문자열 배열 words 가 주어짐
# 문자열의 모든 문자가 allowed 에 있다면 그 문자열은 consistent
# words 에서 consitent string 의 개수를 반환

# 풀이
# 단어의 문자들이 allowed 에 포함되는지 확인


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            if all([c in allowed for c in word]):
                cnt += 1
        return cnt
