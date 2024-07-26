# 문제
# 주어진 트리가 height-balanced 인지 반환
# height-balanced binary tree 는 모든 노드에 대해 왼쪽 서브트리와 오른쪽 서브트리의 높이가 1 이하로 차이나야 함
# A height-balanced binary tree is a binary tree in which **the depth of the two subtrees of every node** never differs by more than one.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True,0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1 # 모든 노드에 대해 균형인지 판단해야 함!!!!
            return [balanced,1+max(left[1],right[1])]
        return dfs(root)[0]