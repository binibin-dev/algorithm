# 문제
# 정수 배열 digits 는 중요한 순으로 정렬됨
# digits 로 표현된 large integer 를 1 증가시키고 그 결과를 배열로 반환

# 풀이
# 각 요소를 string으로 연결 후 int 타입으로 변환하여 1 증가
# 위에서 했던 과정을 반대로 반복하여 정수 배열 형태로 반환

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        large_int = int(''.join(map(str, digits))) + 1
        return list(map(int, list(str(large_int))))