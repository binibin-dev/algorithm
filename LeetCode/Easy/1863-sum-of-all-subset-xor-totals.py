# 문제
# 배열의 XOR total 은 모든 요소의 bitwise XOR 연산으로 정의됨
# 배열이 비어 있다면 0, 아니라면 nums[0] XOR nums[1] XOR ... XOR nums[n]
# 배열 nums 가 주어졌을 때, nums 의 모든 부분집합의 XOR totals 의 합을 반환

# 풀이
# 공집합부터 시작
# 이전 단계에서 나온 부분집합들의 xor 값과 그 부분집합에 다시 원소와 xor 연산한 결과를 합치는 과정을 반복
# [[] -> [[], [A]] -> [[], [A], [B], [AB]] -> [[], [A], [B], [AB], [C], [AC], [BC], [ABC]]
# [0 -> [0, 0^A] -> [0, 0^A, 0^B, 0^A^B] -> [0, 0^A, 0^B, 0^A^B, 0^C, 0^A^C, 0^B^C, 0^A^B^C]


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_totals = [0]
        result = 0

        for n in nums:
            size = len(xor_totals)
            for i in range(size):
                xor_totals.append(xor_totals[i] ^ n)
        
        return sum(xor_totals)