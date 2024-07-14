# 문제
# 빌트인 해쉬 테이블 라이브러리를 사용하지 않고 hashmap 을 만들어야 함.
# add 메서드는 해시 맵에 키-값 쌍을 삽입 (키가 이미 존재하면 값을 업데이트)
# get 메서드는 키가 매핑된 값을 반환 (키가 없으면 -1을 반환)
# remove 메서드는 해시 맵에서 주어진 키가 존재하면 키와 값을 삭제
# At most 10**4 calls will be made to put, get, and remove.

# 해시 함수 필요

class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.buckets = [[]*i for i in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, b in enumerate(bucket):
            if b[0] == key: # key 가 있는 경우 해당 위치에 키와 값을 넣음
                bucket[i] = [key, value]
                return
        bucket.append([key, value]) # key 가 없는 경우 끝에 키와 값을 추가

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b[0] == key:
                return b[1]
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b[0] == key:
                bucket.remove(b)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)