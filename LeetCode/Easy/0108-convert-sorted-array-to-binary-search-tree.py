# 문제
# 오름차순으로 정렬된 정수 배열 nums 가 주어짐
# 이것을 균형 이진 탐색 트리로 변환

# 풀이
# 중간값을 루트로 만듦
# 루트의 왼쪽 서브트리에 재귀 함수를 사용하여 mid 직전까지의 요소들을 노드로 추가
# 루트의 오른쪽 서브트리에 재귀 함수를 사용하여 mid+1부터 마지막 요소들을 노드로 추가

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) # mid 는 이미 루트노드로 넣었으니 mid 는 제외해야 함
        return root