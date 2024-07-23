# 왼쪽 서브트리는 오른쪽 서브트리의 mirror reflection 이어야 함
# 따라서 재귀적으로 함수를 호출할 때는
# 왼쪽 서브트리의 왼쪽 노드와 오른쪽 서브트리의 오른쪽 노드가 같은지 비교 하고, (바깥쪽)
# 왼쪽 서브트리의 오른쪽 노드와 오른쪽 서브트리의 왼쪽 노드가 같은지 비교 (안쪽)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)
    
    def isSame(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if not leftroot or not rightroot:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)