# 문제
# 주어진 연결 리스트에서 노드의 값이 정수 val 과 같으면 삭제

# 풀이
# head.next.val 이 val 이면 해당 노드를 삭제하기 위해 head.next 에 head.next.next 를 넣음
# val 과 다를 때도 다음 노드를 확인할 수 있도록 업데이트 해야 함


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next