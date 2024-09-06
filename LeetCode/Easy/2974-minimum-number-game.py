# 문제
# 길이가 짝수인 정수 배열 nums 가 주어짐
# Alice 와 Bob 은 한 차례마다 모두 한번씩 이동하는 게임을 하기로 함
# 매 차례마다, Alice 는 nums 의 가장 작은 수를 제거, Bob 또한 똑같이 함
# Bob 은 빈 배열 arr 에 이전에 제거했던 요소를 추가, Alice 또한 똑같이 함
# nums 가 빈 상태가 될 때까지 반복
# 결과 arr 를 반환

# 풀이
# 작은 값을 찾는 과정이 계속 반복되므로, 반복문을 돌기 전 nums 를 정렬하여 맨 앞 요소가 작은 값이 되도록 함
# 참고로 요소를 삭제 후, 해당 요소를 append 해야 하므로 pop 메서드를 사용


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        while nums:
            a = nums.pop(0)
            b = nums.pop(0)
            arr.append(b)
            arr.append(a)
        return arr