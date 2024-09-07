# 문제
# 문자열 배열 word1, word2 가 주어짐
# 두 배열이 같은 문자열을 나타내면 true, 아니면 false 를 반환
# 문자열은 배열에 있는 모든 요소를 순서대로 합쳤을 때의 결과임


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)