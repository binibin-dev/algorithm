# 문제
# 주어진 문자열에서 모음만 역순으로 순서를 바꿔 반환

# 풀이
# vowels 에 포함되는 문자만 인덱스를 딕셔너리로 저장 후 키(인덱스) 기준으로 정렬
# i번째 모음과 -i-1(뒤에서 i)번째 모음을 서로 바꿈

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        vowels = ['a', 'e', 'i', 'o', 'u']
        d = {i: c for i, c in enumerate(s) if c.lower() in vowels}
        idx_list = sorted(d.keys())
        
        for i in range(len(idx_list)//2):
            # idx 리스트의 [i] [-i-1] 번째에 있는 vowel 을 서로 바꿈
            s[idx_list[i]] = d[idx_list[-i-1]]
            s[idx_list[-i-1]] = d[idx_list[i]]

        return "".join(s)