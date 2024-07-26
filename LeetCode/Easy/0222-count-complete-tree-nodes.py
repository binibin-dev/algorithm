# 문제
# 완전 이진트리가 주어짐
# 트리의 노드 개수를 반환

# 풀이
# BFS 로 풀다가 큐에 아무것도 남아 있지 않으면 노드 개수를 반환
# root 노드가 없다면 0을 반환
# root 노드가 있다면 노드 개수를 1로 초기화 하고, left나 right 가 있을 때마다 1을 더함

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        number = 1

        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
                number += 1
            if node.right:
                q.append(node.right)
                number += 1

        return number
            