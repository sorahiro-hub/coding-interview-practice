# Problem: Longest Substring Without Repeating Characters
# Description: 与えられた文字列の中で、重複しない最長の部分文字列の長さを返す
# Date: 2025-07-14
# Tags: スライディングウィンドウ, セット, 最長部分列

def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage
if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3
    print(lengthOfLongestSubstring("bbbbb"))     # 1
    print(lengthOfLongestSubstring("pwwkew"))    # 3
    print(lengthOfLongestSubstring(""))          # 0
