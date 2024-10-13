# 문제
# 두 개의 스택을 사용하여 LIFO 큐를 구현
# 구현된 큐는 아래의 함수를 지원해야 함
# - push(x): 큐의 맨 뒤에 요소를 삽입
# - pop(): 큐의 맨 앞에 있는 요소를 삭제하고 해당 요소를 반환
# - peak(): 큐의 맨 앞에 있는 요소를 반환
# - empty(): 큐가 비어 있다면 true, 아니라면 false 를 반환

# 풀이
# 인스턴스를 생성할 때 리스트를 초기화
# pop: 맨 앞에 있는 요소를 제거 후 반환
# peak: 맨 앞에 있는 요소를 반환
# empty: deque 의 크기가 1 이상이면 false 를 반환


class MyQueue:

    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return False if len(self.queue) >= 1 else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()