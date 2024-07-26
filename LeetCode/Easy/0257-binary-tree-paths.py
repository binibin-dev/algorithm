# 문제
# 주어진 이진 트리에서 루트 노드부터 리프 노드까지의 모든 경로를 반환 (순서는 상관 없음)

# q 에 노드와 노드까지의 경로를 담은 리스트를 함께 삽입
# 만약 노드의 왼쪽, 오른쪽 자식 노드가 모두 없으면 리프 노드이므로 경로를 문자열로 묶어 paths 에 삽입
# q 가 빌 때까지 반복

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        q = deque([(root, [root.val])])

        while q:
            node, path = q.pop()
            if not node.left and not node.right:
                path = map(str, path)
                paths.append('->'.join(path))
            
            if node.left:
                q.append([node.left, path + [node.left.val]])
            if node.right:
                q.append([node.right, path + [node.right.val]])

        return paths