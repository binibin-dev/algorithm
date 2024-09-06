# 문제
# 두 이진트리 original 과 cloned, original 의 노드 target 에 대한 참조가 제공됨
# cloned 는 original 을 복사한 것
# cloned 에서 같은 노드에 대한 참조를 반환
# original, cloned, target 을 변경해서는 안 됨

# 풀이
# BFS 로 target.val 과 같은 값을 가지는 노드가 있는지 확인


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned.val:
            return []

        result = deque([cloned])
        
        while result:
            node = result.pop()
            if node.val == target.val:
                return node
            
            if node.left:
                result.append(node.left)
            if node.right:
                result.append(node.right)