
def longestCommonPrefix(strs):
    """
    文字列のリスト strs において、すべての文字列に共通する
    最長の接頭辞（prefix）を返す。
    共通する接頭辞が存在しない場合は、空文字列 "" を返す。
    """

    # 入力が空のリストなら空文字列を返す
    if not strs:
        return ""

    # 最初の文字列を基準の prefix として使う
    prefix = strs[0]

    # 2つ目以降の文字列と順に比較していく
    for word in strs[1:]:
        # 現在の prefix が一致しなくなるまで削る
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # 末尾を1文字ずつ削っていく

            # 削りきった結果、共通部分が無ければ終了
            if not prefix:
                return ""

    # すべての文字列に共通する接頭辞が残る
    return prefix


# ✅ テストコード
if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))  # → "fl"
    print(longestCommonPrefix(["dog", "racecar", "car"]))     # → ""
    print(longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  # → "inters"
    print(longestCommonPrefix(["a"]))  # → "a"
