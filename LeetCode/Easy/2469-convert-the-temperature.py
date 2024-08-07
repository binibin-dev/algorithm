# 문제
# 소수점 이하 두 자리에서 반올림된 음수가 아닌 부동소수점 수 celsius 가 주어짐
# 섭씨(Celsius) 를 켈빈(Kelvin)과 화씨(Fahrenheit) 로 변환하여 [kelvin, fahrenheit] 형태로 반환
# Answers within 10^{-5} of the actual answer will be accepted.
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)]