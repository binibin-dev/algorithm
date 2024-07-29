# 문제
# 주어진 연결 리스트가 회문이라면 True 아니라면 False 를 반환

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        return li == li[::-1]