# 문제 요약
# - 주어진 단어들에서 가장 긴 접두사를 반환해야 함
# - 단어는 하나 이상, 각 단어는 0글자 이상 주어짐

# 풀이
# - 각 단어의 길이가 달라서 index out of range 문제가 있을 것 같음
# - 가장 긴 접두사가 가질 수 있는 최대 길이는 **strs 에 있는 단어 중 가장 짧은 단어의 길이**다. 
# - 따라서 가장 짧은 단어의 길이만큼 한 글자씩 비교한다.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        if "" in strs:
            return ""

        min_length = min(map(lambda s: len(s), strs)) # 가장 작은 단어의 길이
        for i in range(min_length):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return prefix
            prefix += c
        
        return prefix
        
