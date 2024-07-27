# 문제
# 이진 탐색 트리가 주어짐
# 서로 다른 노드 간의 절대차 중 가장 작은 값을 반환

# 풀이
# 노드와 노드까지의 경로를 함께 저장
# 현재 노드의 값과 경로에 있는 노드들의 값 사이의 절대차를 구함
# 이전에 구했던 절대차와 비교하여 작은 값으로 업데이트

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        minVal = float("inf")
        q = deque([(root, [root.val])])

        while q:
            node, path = q.pop()

            if node.left:
                minVal = min([minVal] + [abs(p - node.left.val) for p in path])
                q.append((node.left, path + [node.left.val]))
            if node.right:
                minVal = min([minVal] + [abs(p - node.right.val) for p in path])
                q.append((node.right, path + [node.right.val]))
        
        return minVal
