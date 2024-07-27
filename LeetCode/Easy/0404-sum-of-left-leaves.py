# 문제
# 주어진 이진 트리의 리프 노드 값의 총합을 반환

# 풀이
# 왼쪽 자식 노드가 리프 노드일 경우 해당 왼쪽 노드를 더함

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leaves = []
        q = deque([root])

        while q:
            node = q.pop()

            if node.left:
                if not node.left.left and not node.left.right:
                    leaves.append(node.left.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return sum(leaves)