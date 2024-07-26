# 문제
# 이진 트리의 root 가 주어짐
# 전위 순회한 결과를 반환

# 풀이
# 노드 자신을 traversal 에 삽입
# 노드의 왼쪽 자식을 전위 순회 (1부터 반복)
# 노드의 오른쪽 자식을 전위 순회 (1부터 반복)
# 모두 끝나면 traversal 반환

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return[]

        traversal = []
        
        def preorder(head):
            traversal.append(head.val)
            if head.left:
                preorder(head.left)
            if head.right:
                preorder(head.right)
            return traversal
        
        return preorder(root)
