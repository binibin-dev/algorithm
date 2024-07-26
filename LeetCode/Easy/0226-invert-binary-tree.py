# 문제
# 주어진 이진트리를 뒤집어 반환

# 문제
# BFS 로 각 수준의 왼쪽 노드(서브트리)와 오른쪽 노드(서브트리)를 바꿈
# 참고로 왼쪽 노드만 있으면 오른쪽 노드로 이동하고,
# 오른쪽 노드만 있으면 왼쪽 노드로 이동
# 이를 큐가 빌 때까지 반복


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        
        while q:
            node = q.pop()
            if node.left and node.right:
                node.left, node.right = node.right, node.left
                q.extend([node.left, node.right])
            else:
                if node.right:
                    node.left = node.right
                    node.right = None
                    q.append(node.left)
                elif node.left:
                    node.right = node.left
                    node.left = None
                    q.append(node.right)

        return root