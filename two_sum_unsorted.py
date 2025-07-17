# Problem: Two Sum - Unsorted Array
# Description: ソートされていない配列の中から、2つの数の和がtargetになるインデックスを返す
# Date: 2025-07-17
# Tags: ハッシュマップ, 探索

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

if __name__ == "__main__":
    print(twoSum([3, 2, 4], 6))  # [1, 2]
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([1, 3, 5, 6], 9))  # [1, 3]
