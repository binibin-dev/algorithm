class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for i in range(low, high+1):
            s = str(i)
            if len(s) == 2:
                if s[0] == s[1]:
                    result += 1
            elif len(s) == 4:
                if int(s[0]) + int(s[1]) == int(s[2]) + int(s[3]):
                    result += 1
        
        return result