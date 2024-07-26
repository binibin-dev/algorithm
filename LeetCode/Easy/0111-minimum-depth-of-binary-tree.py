# 문제
# 주어진 이진 트리의 최소 깊이를 구함

# 풀이
# BFS 로 한 수준의 노드들을 차례대로 탐색하면서 depth 를 계산
# 왼쪽, 오른쪽 노드가 모두 없는 경우 1을 반환 (노드 자신의 깊이)
# 왼쪽, 오른쪽 노드 중 하나만 있는 경우는 해당 노드의 깊이를 반환


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        if not root.left: # 오른쪽 노드만 있는 경우
            return 1 + rightDepth
        if not root.right:
            return 1 + leftDepth
        
        return 1 + min(leftDepth, rightDepth)
        


        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))# 작은 depth 를 반환