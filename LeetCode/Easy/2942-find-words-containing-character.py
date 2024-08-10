# 문제
# 문자열 words 와 문자 x 가 주어짐
# words 중 x 가 포함된 단어의 인덱스들을 반환

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]