# 문제
# 1 부터 n 이 매겨진 n 개의 노드로 구성된 방향이 없는 star 그래프가 있음
# star 그래프란 중심에 하나의 노드가 있고 나머지 노드는 중심 노드에만 연결되어 있는 그래프
# 노드 사이에 있는 간선들을 나타내는 2차원 정수 배열 edges 이 주어짐
# star 그래프의 중심을 반환


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]