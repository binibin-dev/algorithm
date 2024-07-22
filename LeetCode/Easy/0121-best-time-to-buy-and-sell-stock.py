# 문제
# 날짜별 주식 가격이 담긴 배열 prices 가 주어짐 (prices[i] 는 i번째 날의 가격)
# 이익을 최대화하는 주식을 살 날짜와 팔 날짜를 골라 최대화된 이익을 반환

# 문제
# 현재 가격에서 이전에 계산했던 최소가격을 뺀 값과 이전에 계산했던 최대 이익 중 큰 값으로 업데이트
# 또한 현재 가격과 이전에 계산했던 최소가격 중 작은 값으로 업데이트

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit