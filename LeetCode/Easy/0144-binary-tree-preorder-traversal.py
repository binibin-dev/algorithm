# 문제
# 이진 트리의 root 가 주어짐
# 선위 순회한 결과를 반환

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return[]

        traversal = []
        
        def preorder(head):
            traversal.append(head.val)
            if head.left:
                preorder(head.left)
            if head.right:
                preorder(head.right)
            return traversal
        
        return preorder(root)
