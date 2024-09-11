# 문제
# 양의 정수 n 이 주어짐
# pivot 정수 x 를 반환
# 1부터 x 사이의 모든 수의 합이 x 와 n 사이에 모든 수의 값과 같을 때 x 는 pivot integer

# 풀이
# sum(range(1, x+1)) == sum(range(x, n+1)) 이라면
# 크기는 range(1, x+1) 보다 range(x, n+1) 가 현저히 적을 것임 (오름차순이기 때문)
# 따라서 오른쪽에서 왼쪽 방향으로 포인터를 이동하면서 pivot integer 를 찾는다.

# leftsum 을 1 부터 n 까지 모든 수의 합으로 초기화
# rightsum 은 n 부터 n 까지 모든 수의 합이므로 n 으로 초기화
# x 는 가장 오른쪽에 있는 n 부터 시작하므로 n 으로 초기화

# 반복하면서
# 1. leftsum 과 rightsum 이 같은 경우 x 를 반환
# 2. leftsum 을 x 만큼 감소
# 3. rightsum 을 x-1 만큼 증가 (leftsum 이 1부터 x-1 사이에 있는 수의 합이기 때문)
# 4. x 을 1 감소


class Solution:
    def pivotInteger(self, n: int) -> int:
        leftsum = sum(range(1, n+1))
        rightsum, x = n, n

        while x:
            if leftsum == rightsum:
                return x
            leftsum -= x
            rightsum += x-1
            x -= 1

        return -1