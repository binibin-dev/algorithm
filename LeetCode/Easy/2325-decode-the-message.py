# 문제
# 문자열 key 와 message 가 주어지며 각각 암호키와 비밀 메세지를 의미
# message 를 복호화하는 과정은 다음과 같음
# 1. 치환표의 순서는 키에 있는 영문 소문자 26자가 모두 처음 등장하는 순서를 사용
# 2. 치환표를 영어 알파벳 순으로 정렬
# 3. message 의 각 문자는 치환표를 사용하여 치환
# 4. 공백은 그대로 유지

# 풀이
# key 로 치환 테이블을 만듦


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        letters = [chr(asc) for asc in range(97, 123)]

        i = 0
        for k in key:
            if k not in d:
                d[k] = letters[i]
                i += 1

        return ''.join([d[c] for c in message])