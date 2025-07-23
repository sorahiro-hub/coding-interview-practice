
def climb_stairs(n):
    """
    配列（DPテーブル）を使って階段を登る通り数を求める。

    Args:
        n (int): 階段の段数（1 <= n <= 45）

    Returns:
        int: 通り数
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    # dp[i] は i段目に到達する方法の数
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 5
    result = climb_stairs(n)
    print(f"{n}段の階段を登る通り数（配列バージョン）: {result}")  # 出力: 8
