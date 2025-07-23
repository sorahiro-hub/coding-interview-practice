def find_max_length(nums):
    """
    0と1が同数となる最長の連続部分配列の長さを求める。

    Args:
        nums (List[int]): 0と1からなる整数配列

    Returns:
        int: 条件を満たす最長部分配列の長さ
    """
    count = 0
    max_len = 0
    sum_index_map = {0: -1}  # 累積カウントが初めて現れたインデックス

    for i, num in enumerate(nums):
        # 0を-1として扱い、累積計算
        count += -1 if num == 0 else 1

        if count in sum_index_map:
            # 同じカウントが前にもあれば、その間は0と1が同数
            max_len = max(max_len, i - sum_index_map[count])
        else:
            # 初めて出たcountのインデックスを記録
            sum_index_map[count] = i

    return max_len


if __name__ == "__main__":
    nums = [0, 1, 0, 0, 1, 1]
    result = find_max_length(nums)
    print("0と1の数が同じ連続部分配列の最大長:", result)  # 出力: 6
