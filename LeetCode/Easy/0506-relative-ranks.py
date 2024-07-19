# 문제
# 정수 배열 score 가 주어지고, 각 요소는 해당 위치의 선수의 점수를 의미
# 각 선수들의 위치는 그들의 순위를 결정함
# 점수가 높은 순대로 각각 Gold Medal, Silver Medal, Bronze Medal
# 네 번째부터는 그냥 등수로 표현
# 각 선수들의 순위를 담은 배열 answer 를 반환

# 풀이
# 딕셔너리에 점수:인덱스 쌍을 저장
# 점수를 역순으로 정렬하여 반복
# 정렬된 점수에서 첫 번째부터 세 번째 점수까지는 메달이름, 그 이후는 순위
# 각 rank 를 넣는 인덱스는 딕셔너리[점수]로 찾음

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = [None] * len(score)
        d = {s: i for i, s in enumerate(score)}

        for r, s in enumerate(sorted(score, reverse=True)):
            if r+1 > 3:
                rank = str(r+1)
            elif r+1 == 3:
                rank = "Bronze Medal"
            elif r+1 == 2:
                rank = "Silver Medal"
            elif r+1 == 1:
                rank = "Gold Medal"
            answer[d[s]] = rank
        return answer