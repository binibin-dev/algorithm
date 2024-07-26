# 문제
# 이진 트리의 root 와 정수 targetSum 이 주어짐
# 루트 노드에서 리프 노드까지의 경로에 있는 값들을 더해서 targetSum 이 나오면 True 를 반환

# 풀이
# 스택에 노드와 해당 노드까지의 경로의 합을 삽입
# 자식 노드가 없고 해당 노드까지의 경로의 합이 targetSum 과 같으면 True 를 반환
# 아니라면 스택에 자식 노드와 자식 노드까지의 경로의 합을 삽입

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()

            if not node.left and not node.right and val == targetSum:
                return True
            
            if node.left:
                stack.append((node.left, val + node.left.val))
            if node.right:
                stack.append((node.right, val + node.right.val))
        
        return False