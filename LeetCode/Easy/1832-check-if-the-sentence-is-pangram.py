# 문제
# pangram 이란 영어 알파벳의 모든 문자가 적어도 한번씩 나오는 문자열
# 문자열 sentence 가 pangram 이라면 true, 아니라면 false 를 반환

# 풀이
# sentence 의 각 문자가 몇 번 나오는지 딕셔너리로 만듦
# 딕셔너리의 키 길이와 영어 알파벳 개수(26)와 같은지 확인


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for c in sentence:
            if c not in d:
                d[c] = 0
            d[c] += 1
        return len(d.keys()) == len(range(ord('a'), ord('z')+1))