# 문제
# Roman numeral 을 정수로 반환
# 기본적으로 앞 문자가 더 큼 (Roman numerals are usually written largest to smallest from left to right.)
# 또한 roman numerals 는 각 문자에 대한 수의 합을 의미

# 앞 문자가 뒷문자보다 작은 경우가 존재
# - V and X 앞에 I가 있는 경우 => 4 and 9
# - L and C 앞에 I가 있는 경우 => 40 and 90
# - D and M 앞에 I가 있는 경우 => 400 and 900

# 풀이
# 즉 앞 문자가 뒷 문자보다 작은 경우에는 앞 문자를 빼고,
# 그 외의 경우(앞 문자가 뒷 문자보다 큰 경우)에는 앞 문자를 더함
# 마지막 문자는 비교할 게 없기 때문에 해당 문자에 대한 값을 더함

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
                
        result += d[s[-1]]
    
        return result
