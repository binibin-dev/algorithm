# 문제
# 이진 탐색 트리의 root 노드와 두 정수 low, high 가 주어짐
# 이진탐색트리에서 low 와 high 사이에 있는 값들의 합을 반환


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        rangeSum = 0
        while queue:
            node = queue.pop()
            if node.val >= low and node.val <= high:
                rangeSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return rangeSum