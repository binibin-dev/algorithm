class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = str(x)
        test = len(string) // 2
        
        for i in range(test):
            if string[i] != string[-(i+1)]:
                return False
        return True