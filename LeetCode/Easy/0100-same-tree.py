# 문제
# 두 이진 트리의 루트 p 와 q 가 주어짐
# 두 이진 트리가 같은지 아닌지를 반환
# 구조적으로 동일하고 노드들이 같은 값을 가져야 같다고 판단함

# self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# 이 부분들은 중간에 False 가 반환되지 않는다면 말단 노드가 없을 때까지 반복하게 됨 => True 반환

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # 모두 없으면 True
            return True
        elif not p or not q: # 둘 중 하나만 없으면 False (같을 수가 없으므로)
            return False
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)