# 문제
# 문자로 구성된 배열 letters 는 오름차순으로 정렬됨
# target 보다 큰 가장 작은 문자를 반환 (사전적 순서(lexicographically)로 따짐)


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]: # target 보다 큰 값이 존재하지 않는 경우
            return letters[0]
        
        left, right = 0, len(letters)-1
        while left < right:
            mid = (right+left)//2
            
            if  target >= letters[mid]: # in binary search this would be only greater than
                left = mid+1
            
            if target < letters[mid]:
                right = mid
                
        return letters[right]