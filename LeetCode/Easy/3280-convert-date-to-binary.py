# 문제
# yyyy-mm-dd 형식의 문자열 date 가 주어짐
# date 는 연도, 월, 일을 앞에 0이 없는 이진 표현으로 변환하여 쓸 수 있음
# date 의 이진 표현을 반환

# 풀이
# -로 split
# 연도, 월, 일 각각을 이진 표현으로 변환
# (bin 함수 사용 시 0b 가 앞에 붙으므로 주의)
# (앞에 있는 0을 없애기 위해 이진 표현으로 바꾼 후 int로 다시 형변환)
# -로 다시 이어 붙임


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        result = []
        for word in date.split('-'):
            res = str(int(bin(int(word))[2:]))
            result.append(res)
        return '-'.join(result)