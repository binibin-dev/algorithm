# 문제
# 배열 items 가 주어짐. (items[i] = [typei, colori, namei])
# 즉 i 번째 아이템의 type, color, name 을 나타냄
# 두 문자열 ruleKey, ruleValue 로 표현되는 규칙이 주어짐
# i 번째 아이템은 아래 중 하나가 true 라면 규칙에 맞는다고 할 수 있음
# - ruleKey == "type" and ruleValue == typei.
# - ruleKey == "color" and ruleValue == colori.
# - ruleKey == "name" and ruleValue == namei.
# 규칙에 맞는 아이템의 개수를 반환


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key = None
        count = 0

        if ruleKey == 'type':
            key = 0
        elif ruleKey == 'color':
            key = 1
        elif ruleKey == "name":
            key = 2
        
        for item in items:
            if item[key] == ruleValue:
                count += 1

        return count