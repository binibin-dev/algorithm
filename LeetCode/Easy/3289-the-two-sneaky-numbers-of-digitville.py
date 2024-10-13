# 문제
# 0부터 n-1 까지의 정수가 포함된 리스트 nums 가 주어짐
# 각 수는 정확히 한번만 나타나야 했지만 두 개의 숫자가 몰래 추가되어 길이가 길어짐
# 몰래 추가된 숫자가 포함된 사이즈가 2인 배열을 반환

# 풀이
# 한번 이상 나타나는 숫자는 몰래 추가된 숫자일 것임
# 따라서 반복문을 돌면서 출현 횟수를 기록하고, 1 이상인 수만 반환


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        return [k for k, v in d.items() if v > 1]