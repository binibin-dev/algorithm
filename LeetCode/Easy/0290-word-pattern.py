# 문제
# pattern 과 s 가 주어지고, s 가 pattern 을 따르는지를 반환

# 풀이
# 패턴의 각 글자가 매칭되는 단어를 키와 값으로 저장하고, 이 과정을 반복
# 즉 키는 패턴의 i 번째 글자, 값은 s 를 공백 기준으로 나눴을 때 i 번째 단어
# 모든 키와 값은 중복되면 안 됨.
# ex) a: dog 가 있다면 b: dog 는 추가될 수 없고, 
#     a: dog 가 추가되었다면 a: cat 는 추가될 수 없음

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        sl = s.split()

        if len(pattern) != len(sl):
            return False

        for i in range(len(sl)): # 단어 개수만큼 반복
            if pattern[i] in d: # 이미 저장된 키가 있고 매핑된 값이 일치하지 않는 경우
                if sl[i] != d[pattern[i]]:
                    return False
            elif sl[i] in d.values(): # 값이 다른 키에 매핑되어 있는 경우
                return False
            else:
                d[pattern[i]] = sl[i]
        return True