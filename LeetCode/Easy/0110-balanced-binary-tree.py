# 문제
# 주어진 트리가 height-balanced 인지 반환
# height-balanced binary tree 는 왼쪽 서브트리와 오른쪽 서브트리의 높이가 1 이하로 차이나야 함

# 풀이
# 이진 탐색 트리는 왼쪽 자식 노드가 부모 노드보다 작고, 오른쪽 자식 노드가 부모보다 커야 함
# 따라서 왼쪽 서브트리와 오른쪽 서브트리의 높이도 확인해야 하고,
# 노드들이 위의 조건을 만족하는지도 확인해야 함

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(head):
            if head is None:
                return 0

            left = depth(head.left)
            right = depth(head.right)

            return 1 + max(left, right)

        if not root:
            return True

        return abs(depth(root.left) - depth(root.right)) <= 1