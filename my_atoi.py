
def myAtoi(s: str) -> int:
    i = 0
    n = len(s)
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # 1. 空白をスキップ
    while i < n and s[i] == ' ':
        i += 1

    # 2. 符号の処理
    sign = 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    # 3. 数字を読み取る
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    # 4. 符号を適用
    result *= sign

    # 5. 範囲を制限
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result


# 使用例（テスト）
if __name__ == "__main__":
    test_cases = [
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332"
    ]
    for s in test_cases:
        print(f'Input: "{s}" → Output: {myAtoi(s)}')
