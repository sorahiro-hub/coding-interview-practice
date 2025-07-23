
def convert(s: str, numRows: int) -> str:
    """
    文字列sをZ字形に並べ、行ごとに読み取って新しい文字列を返す。
    """
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    result = convert(s, numRows)
    print("Z字変換結果:", result)  # 出力: PAHNAPLSIIGYIR
