# 문제
# 문자열 command 를 해석할 수 있는 goal parser 가 있음
# command 는 "G", "()" and/or "(al)" 로 구성
# goal parser 는 "G" 는 "G", "()" 는 "o", "(al)" 는 "al"로 해석


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')