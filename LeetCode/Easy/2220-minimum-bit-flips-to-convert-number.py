# 문제
# 숫자 x 의 bit flip 이란 x 의 이진 표현에서 하나의 비트를 0 to 1 또는 1 to 0 으로 변환하는 것
# 표시되지 않은 0을 포함
# 두 정수 start 와 goal 이 주어짐
# start 를 goal 로 변환하기 위한 최소의 bit flip 횟수를 반환

# 풀이
# start 와 goal 을 이진 표현으로 변환 후 서로 다른 문자의 개수를 찾으면 됨 ('0b' 제거 필요)
# 정확한 비교를 위해서 이진 표현의 길이를 맞춰줘야 함


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        sbin = bin(start).lstrip('0b')
        gbin = bin(goal).lstrip('0b')

        if len(sbin) >= len(gbin):
            gbin = '0'*(len(sbin)-len(gbin)) + gbin
        else:
            sbin = '0'*(len(gbin)-len(sbin)) + sbin

        flips = [s!=g for s, g in zip(sbin, gbin)]

        return sum(flips)