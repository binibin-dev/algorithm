# 문제
# 정렬된 두 연결 리스트가 주어짐
# 두 리스트를 하나의 정렬된 리스트로 병합해야 함

# 풀이
# cur 는 현재 위치, head 는 시작 노드
# 반복할 때마다 list1 과 list2의 요소를 비교하여 작은 값을 가진 노드로 cur.next 를 가리킴
# 이 과정을 한 리스트가 끝까지 도달할 때까지 반복 (정렬된 상태기 때문에 남은 나머지는 그대로 이어 붙임)
# head.next 를 반환 (the actual list starts at head.next)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next # cur.next 에 넣은 노드의 다음 위치(list1.next)로 업데이트
            else:
                cur.next = list2
                list2 = list2.next # cur.next 에 넣은 노드의 다음 위치(list2.next)로 업데이트
            
            cur = cur.next
        
        cur.next = list1 if list1 else list2
        
        return head.next