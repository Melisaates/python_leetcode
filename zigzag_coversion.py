#1h 45min
#1.way- Zigzag Conversion
# time complexity: O(n)
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        table = [[None] * n for _ in range(numRows)]

        row = 0
        col = 0
        going_down = True   # sadece durum, direction yok

        for ch in s:
            table[row][col] = ch

            # Aşağı gidiyoruz
            if going_down:
                if row == numRows - 1:
                    going_down = False
                    row -= 1
                    col += 1
                else:
                    row += 1

            # Çapraz yukarı gidiyoruz
            else:
                if row == 0:
                    going_down = True
                    row += 1
                else:
                    row -= 1
                    col += 1

        # Satır satır oku
        result = ""
        for r in range(numRows):
            for c in range(n):
                if table[r][c] is not None:
                    result += table[r][c]

        return result

#2.way- Zigzag Conversion
# time complexity: O(n)
# optimized space complexity: O(n)
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        going_down = True

        for ch in s:
            rows[row] += ch

            if row == 0:
                going_down = True
            elif row == numRows - 1:
                going_down = False

            row += 1 if going_down else -1

        return "".join(rows)
