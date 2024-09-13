# 문제
# 양의 정수 배열 nums 가 주어짐
# Alice 는 nums 로부터 모든 한 자리 수를 선택하거나 모든 두 자리 수를 선택할 수 있음
# 남은 숫자들이 Bob 에게 주어짐
# 가진 숫자들의 합이 큰 사람이 이김
# Alice 가 게임에서 이긴다면 true, 아니라면 false 를 반환

# 풀이
# nums 의 각 수를 문자열로 변환 후 자릿수를 확인하여 따로 저장
# 한 자릿수의 합과 두 자릿수의 합이 서로 다르다면 true 를 반환
# 서로 다르다면 어느 하나는 더 크다는 의미이기 때문


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        for i in range(len(nums)):
            if len(str(nums[i])) == 1:
                single.append(nums[i])
            else:
                double.append(nums[i])
        return sum(single) != sum(double)