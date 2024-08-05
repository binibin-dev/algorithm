# 문제
# 주어진 이진트리가 이진탐색 트리인지 아닌지 반환
# 모든 노드에 대해 왼쪽 서브트리의 키는 노드의 키보다 작음
# 모든 노드에 대해 오른쪽 서브트리의 키는 노드의 키보다 큼

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, min_val=float("-inf"), max_val=float("inf")):
            if not root:
                return True

            if not (min_val < root.val < max_val):
                return False
            
            return bst(root.left, min_val, root.val) and bst(root.right, root.val, max_val)
        
        return bst(root)