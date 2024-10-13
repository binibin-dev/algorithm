# 문제
# 두 개의 큐를 사용하여 LIFO 스택을 구현
# 구현된 스택은 아래의 함수를 지원해야 함
# - push(x): 스택의 맨 위에 요소를 삽입
# - pop(): 스택의 맨 위에 있는 요소를 삭제하고 해당 요소를 반환
# - top(): 스택의 맨 위에 있는 요소를 반환
# - empty(): 스택이 비어 있다면 true, 아니라면 false 를 반환

# 풀이
# 인스턴스를 생성할 때 deque 를 초기화
# top: 가장 마지막 인자를 반환
# empty: deque 의 크기가 1 이상이면 false 를 반환


class MyStack:

    def __init__(self):
        self.stack = deque()
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return False if len(self.stack) >= 1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()