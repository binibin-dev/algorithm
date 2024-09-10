# 문제
# 정확히 3개의 노드로 구성된 이진 트리의 root 가 주어짐 (root, left child, right child)
# 루트의 값이 가 두 자식 노드의 합과 같다면 True, 아니라면 False 를 반환


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)