
from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    与えられた整数リスト nums の中で、最も頻度の高い k 個の要素を返す。

    引数:
        nums: List[int] - 数のリスト
        k: int - 頻度上位 k 個を取得したい

    戻り値:
        List[int] - 頻度が高い順に k 個の要素を含むリスト
    """
    # ① Counter を使って各要素の出現回数を辞書としてカウント
    count = Counter(nums)  # 例: {1: 3, 2: 2, 3: 1}

    # ② heapq.nlargest を使って、辞書のキーの中から頻度が高い順に k 個取得
    #    key=count.get により、辞書の「値」（=出現回数）を比較基準にしている
    return heapq.nlargest(k, count.keys(), key=count.get)


# ✅ 使用例・テストコード
if __name__ == "__main__":
    # 例1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print("出力例1:", topKFrequent(nums1, k1))  # → [1, 2]

    # 例2
    nums2 = [1]
    k2 = 1
    print("出力例2:", topKFrequent(nums2, k2))  # → [1]
