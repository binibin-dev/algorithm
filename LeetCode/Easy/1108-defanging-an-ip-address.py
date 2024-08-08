# 문제
# 유효한 (IPv4) IP 인 address 가 주어짐
# 모든 . 을 [.] 으로 변형하여 반환

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')