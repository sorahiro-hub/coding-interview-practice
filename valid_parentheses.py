# Problem: Valid Parentheses
# Description: 与えられたカッコ列が正しく閉じられているかを判定する
# Date: 2025-07-17
# Tags: スタック, 対応判定, 文字列処理

def isValid(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()

    return not stack

if __name__ == "__main__":
    print(isValid("()[]{}"))    # True
    print(isValid("([)]"))      # False
    print(isValid("{[]}"))      # True
    print(isValid("((("))       # False
    print(isValid("((){})[]"))  # True
