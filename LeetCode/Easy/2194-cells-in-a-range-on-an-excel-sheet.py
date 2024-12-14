# 문제
# 하나의 셀(r, c)은 <열번호><행번호> 로 표현됨
# 열 번호는 알파벳 문자이며, 행 번호는 정수 숫자
# <col1><row1>:<col2><row2> 형태의 문자열 s 가 주어짐
# c1 <= c2 and r1 <= r2
# 두 셀을 포함하여 사이에 있는 셀의 리스트를 반환
# 반환되는 셀들은 <열번호><행번호> 형태여야 하며, 열을 우선으로 오름차순 정렬되어야 함
# s의 길이는 5, 열번호는 A에서 Z 사이, 행 번호는 1에서 9 사이

# 문제
# :로 나눠 두 셀을 구분
# 행과 열을 구분



class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = s.split(':')
        start_col, start_row = cells[0][0], cells[0][1]
        end_col, end_row = cells[1][0], cells[1][1]
        
        results = []
        for c in range(ord(start_col), ord(end_col) + 1): # 열부터 반복
            col = chr(c)
            for r in range(int(start_row), int(end_row) + 1):
                row = str(r)
                results.append(col+row)
        
        return results