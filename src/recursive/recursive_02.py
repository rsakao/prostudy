# 問題2: リストの合計
# 与えられた整数のリストの合計を計算する再帰関数を書いてください。

def sum_list(list):
  if len(list) == 0:
    return 0
  return list[0] + sum_list(list[1:])
