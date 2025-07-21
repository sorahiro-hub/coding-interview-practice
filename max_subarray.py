
def max_subarray(nums):
    """
    Kadane's Algorithm を使って、連続部分配列の最大和を求める。
    """
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray(nums)
    print("最大部分配列和:", result)
