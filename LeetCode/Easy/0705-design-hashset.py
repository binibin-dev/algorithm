# 문제
# 빌트인 해쉬 테이블 라이브러리를 사용하지 않고 hashSet 을 만들어야 함.
# add 함수는 해시 셋에 값을 삽입
# contains 함수는 해시셋에 주어진 키의 존재 여부를 반환
# remove 함수는 해시셋에서 주어진 키를 삭제, 키가 존재하지 않으면 아무것도 하지 않음


class MyHashSet:

    def __init__(self):
        self.buckets = []

    def add(self, key: int) -> None:
        if key not in self.buckets:
            self.buckets.append(key)

    def remove(self, key: int) -> None:
        if key in self.buckets:
            self.buckets.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)