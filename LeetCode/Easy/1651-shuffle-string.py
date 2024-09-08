# 문제
# 서로 같은 길이인 문자열 s 와 정수 배열 indices 가 주어짐
# 문자열 s 는 i 번째 있는 문자가 인덱스 indices[i] 에 위치하도록 섞은 결과를 반환


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(indices)
        for i, c in enumerate(s):
            result[indices[i]] = s[i]
        return ''.join(result)