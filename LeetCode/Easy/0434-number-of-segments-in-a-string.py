# 문제
# segment 의 개수를 반환
# segment 란 공백이 없이 이어진 sequence 를 말함

# 풀이
# 공백 기준으로 나눠 개수를 셈

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())