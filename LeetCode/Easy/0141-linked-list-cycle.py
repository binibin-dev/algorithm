# 문제
# 연결 리스트가 주어졌을 때, 순환이 존재하는지 반환
# 내부적으로  pos는 가장 마지막 노드의 next 포인터가 **연결된 노드의 인덱스**를 나타냄

# 풀이
# 속도가 다른 두 포인터(tortoise(slow), hare(fast))를 사용
# tortoise 는 한 칸씩 이동, hare 는 두 칸씩 이동
# 순환이 없다면 hare 는 언젠가 null 에 도달하므로 루프를 중단
# 순환이 있다면 hare 와 tortoise 는 언젠가 루프에서 만날 것임


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False