/

# Problem: Group Anagrams
# Description: グループ内でアナグラムの単語をまとめる
# Date: 2025-07-14
# Tags: ハッシュマップ, ソート, defaultdict

from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# Example usage
if __name__ == "__main__":
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(test_input))
