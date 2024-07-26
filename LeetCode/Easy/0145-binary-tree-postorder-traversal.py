# 문제
# 이진 트리의 root 가 주어짐
# 후위 순회한 결과를 반환

# 풀이
# 노드의 왼쪽 자식을 후위 순회
# 노드의 오른쪽 자식을 후위 순회
# 노드 자신을 traversal 에 삽입
# 모두 끝나면 traversal 반환

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        traversal = []

        def postorder(head):
            if head.left:
                postorder(head.left)
            if head.right:
                postorder(head.right)
            traversal.append(head.val)
            return  traversal
        
        return postorder(root)