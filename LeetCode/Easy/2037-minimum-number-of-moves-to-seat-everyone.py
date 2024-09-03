# 문제
# 길이가 n 인 배열 seats 와 길이가 n 인 배열 students 가 주어짐
# seats[i] 는 i 번째 좌석의 위치
# students[j] 는 j 번째 학생의 위치
# 특정 학생의 위치를 1씩 증가 또는 감소하여 이동할 수 있음
# 두 학생이 같은 좌석에 앉지 않도록 각 학생을 이동해야 하며, 최소 이동 횟수를 반환

# 풀이
# seats 와 students 를 모두 정렬하여 students[i] 가 seats[i] 에 앉으려면 이동해야 하는 횟수를 모두 더함


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        minMoves = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            minMoves += abs(seats[i] - students[i])
        return minMoves