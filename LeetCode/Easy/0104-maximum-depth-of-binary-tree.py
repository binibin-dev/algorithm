# 문제
# 이진 트리의 최대 깊이를 반환
# 이진 트리의 최대 깊이란 루트 노드에서 가장 먼 리프 노드까지의 가장 긴 경로에서의 노드 개수

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1