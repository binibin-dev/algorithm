# 문제
# 주어진 연결 리스트를 뒤집어 반환

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # recursion
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head and head.next:
    #         new = self.reverseList(head.next)
    #         head.next.next, head.next = head, None
    #         head = new
    #     return head
    
    # iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev