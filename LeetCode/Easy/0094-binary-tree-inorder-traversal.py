# 왼쪽 서브트리 -> 루트 노드 -> 오른쪽 서브트리 순서로
# inorder 순회를 재귀 호출

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)
        traverse(root)
        return result