# 문제
# 테이블에 n 개의 돌(무더기)이 있음
# 상대와 나의 차례가 번갈아가면서 돌아오며, 내가 먼저임
# 본인 차례에는 돌 무더기에서 1~3개의 돌을 없앰
# 마지막 돌을 없애는 사람이 이김
# 내가 승리할 수 있다면 True, 아니라면 False
# assuming both you and your friend play optimally

# 풀이
# 내가 이기는 경우는 내 차례에 1~3개 남아 있는 경우임
# 4: 몇 개를 가져가더라도 무조건 짐
# 5: 1 3 1 => win
# 6: 2 3 1 = > win
# 즉, n 이 4로 나눠 딱 떨어지면 내 차례에 4개가 남는 순간이 돌아옴

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0