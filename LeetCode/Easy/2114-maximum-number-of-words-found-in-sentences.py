# 문제
# sentence 란 하나의 공백으로 구분된 단어들의 나열
# 문자열 배열 sentences 가 주어짐
# sentences[i] 는 하나의 문장을 의미
# 한 문장에서 나오는 가장 많은 단어 개수를 반환


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split()) for s in sentences])