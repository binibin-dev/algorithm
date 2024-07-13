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
        