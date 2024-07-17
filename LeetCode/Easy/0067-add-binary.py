# 문제
# 두 바이너리 스트링을 더하여 반환

# 2진수로 변환하여 더하고, 더한 값을 다시 이진수로 변환하여 반환

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)
        z = x + y
        return bin(z)[2:] # 0x 제거