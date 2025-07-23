
def climb_stairs(n):
    """
    配列を使わずに階段を登る通り数を求める（フィボナッチ的DP）

    Args:
        n (int): 階段の段数（1 <= n <= 45）

    Returns:
        int: 通り数
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    one_step_before = 2  # dp[i - 1]
    two_steps_before = 1 # dp[i - 2]

    for i in range(3, n + 1):
        current = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before


if __name__ == "__main__":
    n = 5
    result = climb_stairs(n)
    print(f"{n}段の階段を登る通り数（変数バージョン）: {result}")  # 出力: 8
