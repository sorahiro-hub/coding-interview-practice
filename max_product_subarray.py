def max_product(nums):
    """
    最大積部分配列の積を求める（Kadane's Algorithmの積バージョン）

    Args:
        nums (List[int]): 整数のリスト

    Returns:
        int: 最大積
    """
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            # 符号が反転する可能性があるので入れ替え
            max_prod, min_prod = min_prod, max_prod

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        result = max(result, max_prod)

    return result


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print("最大積部分配列の積:", max_product(nums))  # 出力: 6
