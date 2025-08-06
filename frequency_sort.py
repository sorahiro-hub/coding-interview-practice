
from collections import Counter

def frequencySort(s):
    """
    文字列 s に含まれる文字を、出現頻度の高い順に並べた文字列を返す。
    例：s = "tree" → 出力: "eert" や "eetr" など
    """

    # Step 1: 各文字の出現頻度をカウント
    counter = Counter(s)  # 例: Counter({'e': 2, 't': 1, 'r': 1})

    # Step 2: 出現頻度の高い順に並び替える（most_common は降順で返す）
    sorted_pairs = counter.most_common()
    # 例: [('e', 2), ('t', 1), ('r', 1)]

    # Step 3: 各文字をその回数だけ繰り返して連結
    result = ''.join([char * freq for char, freq in sorted_pairs])
    # 例: "ee" + "t" + "r" → "eert"

    return result


# ✅ テスト用コード
if __name__ == "__main__":
    print(frequencySort("tree"))     # → "eert" や "eetr"
    print(frequencySort("cccaaa"))   # → "aaaccc" や "cccaaa"
    print(frequencySort("Aabb"))     # → "bbAa" など
