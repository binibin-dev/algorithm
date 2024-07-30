# 문제
# 사람 이름이 담긴 배열 names 와 사람의 키가 담긴 배열 heights 가 주어짐 (길이는 동일)
# names[i] 와 heights[i] 는 i 번째 사람에 대한 정보
# 키가 작은 순서대로 names 를 정렬

# 정렬 기준이 될 배열을 앞에 두어 두 배열을 zip
# 내림차순으로 정렬 후 정렬된 name 들을 반환

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # people = list(zip(heights, names)) # heights 기준으로 정렬되어야 하기 때문에 heights 를 앞에 둠
        # people.sort(reverse=True)
        return [name for _, name in sorted(list(zip(heights, names)), reverse=True)]