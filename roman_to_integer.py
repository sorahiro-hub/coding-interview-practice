
def romanToInt(s):
    """
    ローマ数字を整数に変換する関数。

    ローマ数字には以下の対応がある：

        I  = 1
        V  = 5
        X  = 10
        L  = 50
        C  = 100
        D  = 500
        M  = 1000

    小さい値が大きい値の前に来るときは「引く」ことで特別な数を表す：
        IV = 4（5 - 1）
        IX = 9（10 - 1）
        XL = 40（50 - 10）
        XC = 90（100 - 10）
        CD = 400（500 - 100）
        CM = 900（1000 - 100）

    これらを考慮して、右から左へ文字を見ながら計算する。
    """

    # ローマ数字と整数の対応辞書を用意
    roman = {
        'I': 1,  'V': 5,  'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0       # 最終的な答えを格納する変数
    prev = 0        # 前回の文字の数値を保存（初期は0）

    # 右から左へループすることで、引き算すべきかを簡単に判断できる
    for c in reversed(s):
        value = roman[c]  # 今の文字の数値を取得

        if value < prev:
            # 小さい値が後ろにある場合 → 引き算
            total -= value
        else:
            # それ以外（大きい値 or 同じ） → 足し算
            total += value

        # 次のループで使うために、今回の値を prev に保存
        prev = value

    return total


# ✅ テストコード（このファイルを実行したときだけ動くようにしている）
if __name__ == "__main__":
    print(romanToInt("III"))      # 出力: 3
    print(romanToInt("IV"))       # 出力: 4
    print(romanToInt("IX"))       # 出力: 9
    print(romanToInt("LVIII"))    # 出力: 58
    print(romanToInt("MCMXCIV"))  # 出力: 1994
