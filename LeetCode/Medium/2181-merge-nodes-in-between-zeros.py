# 문제
# 0으로 분리되는 정수의 나열을 포함한 연결 리스트의 head 가 주어짐
# 연결 리스트의 시작과 끝은 Node.val == 0
# 0 과 0 사이에 있는 노드의 값의 합이 하나의 노드의 값이 되도록 합쳐 연결 리스트를 수정하여 반환
# 수정된 연결 리스트에는 0이 포함되지 않아야 함

# 풀이
# 더미 노드를 만들어 시작 위치를 기억
# num 에는 0과 0 사이에 있는 노드의 값의 합을 저장할 것임
# 노드의 값이 0이면서 num가 0이면 합칠 리스트의 시작
# 노드의 값이 0이면서 num가 0이 아니면 합칠 리스트의 끝이므로 결과 헤드에 num 을 값으로 갖는 노드를 추가
# 노드의 값이 0이 아닌 경우 num 에 노드의 값을 더함
# 탐색할 노드를 다음 노드로 업데이트


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        
        dummy = node = ListNode()
        num = 0

        while head:
            if head.val == 0:
                if num != 0:
                    node.next = ListNode(val=num)
                    node = node.next
                    num = 0
            else:
                num += head.val
            head = head.next

        return dummy.next
