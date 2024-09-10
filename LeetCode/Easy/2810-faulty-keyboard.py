# 문제
# 랩탑의 키보드가 불완전한 상태이며 'i' 를 입력할 때마다 작성했던 문자열이 뒤집힘
# 문자열 s 가 주어지고, 불완전한 키보드를 사용해 s 의 각 문자를 입력
# 화면에 보일 최종 문자열을 반환


class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for c in s:
            if c == 'i':
                result.reverse()
            else:
                result.append(c)
        return ''.join(result)