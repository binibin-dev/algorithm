# 정렬된 연결 리스트의 head가 주어지면 각 요소가 한 번만 나오도록 정렬하여 반환

# 반환할 때는 원본(head)을 반환해야 함!!!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head