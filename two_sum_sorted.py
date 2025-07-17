# Problem: Two Sum II - Input Array Is Sorted
# Description: ソート済み配列から、2つの数の和がtargetになるインデックスを返す
# Date: 2025-07-17
# Tags: 2ポインタ, ソート済み配列

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(twoSum([1, 2, 3, 4], 5))    # [1, 4]
    print(twoSum([1, 3, 4, 5, 7, 10], 13))  # [3, 6]
