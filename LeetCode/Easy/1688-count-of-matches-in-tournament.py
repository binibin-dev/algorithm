# 문제
# 토너먼트에 있는 팀의 개수인 정수 n 이 주어짐
# 토너먼트에는 아래와 같은 규칙이 있음
# 팀 수가 짝수라면
# - 각 팀은 또 다른 팀과 묶임.
# - n/2 번만큼 경기가 진행되어 n/2 개의 팀이 다음 라운드로 진출
# 팀 수가 홀수라면
# - 랜덤하게 한 팀은 토너먼트에서 진출하고, 나머지는 쌍이 지어짐.
# - (n-1)/2 번 경기가 진행되며 한 팀이 부전승하였기 때문에 (n-1)/2+1 팀이 다음 라운드로 진출함
# 승자가 결정될 때까지 토너먼트에서 진행된 경기 횟수를 반환

# 풀이
# team 수를 업데이트하기 전에 경기 수를 먼저 구해줘야 함


class Solution:
    def numberOfMatches(self, n: int) -> int:
        team = n
        matches = 0

        while team > 1:
            if team % 2 == 0:
                matches += team/2
                team = team/2
            else:
                matches += (team-1)/2
                team = (team-1)/2+1

        return int(matches)
                