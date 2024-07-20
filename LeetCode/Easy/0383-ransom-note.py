# 문제
# magazine 에 있는 문자로 ransomNote 를 만들 수 있으면 True 를 반환
# magazine 에 있는 문자는 ransomNote 에서 한번만 쓰일 수 있음

# 풀이
# magazine 을 리스트로 변환 (ransomeNote 에 포함되는 문자를 삭제하기 위함)
# ransomNote 의 각 문자가 magazine 내에 있는지 확인
# 만약 magazine 에 있다면 해당 문자를 삭제
# magazine 에 포함되지 않는 문자가 있다면 False 를 반환

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for c in ransomNote:
            if c in magazine:
                magazine.remove(c)
            else:
                return False
        return True