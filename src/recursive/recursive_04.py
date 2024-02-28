# 問題4: 二分探索
# ソートされた配列と目的の値が与えられたとき、その値のインデックスを返す二分探索の再帰関数を書いてください。その値が配列に存在しない場合は、-1を返してください。

def binary_search(arr, target, index=0):
  if len(arr) == 0 or (len(arr) == 1 and arr[0] != target):
    return -1

  # 真ん中で分ける
  center_index = len(arr) // 2
  center_num = arr[center_index]
  # 真ん中の値がターゲットと一致するかどうかを確認
  # 一致したらそのインデックスを返す
  if center_num == target:
    return center_index + index

  # 一致しなかったら、真ん中の値がターゲットより大きいか小さいかを確認
  if center_num < target:
    # ターゲットが真ん中の値より大きい場合は、真ん中より右側の部分配列を再帰的に探索
    if len(arr) <= center_index + 1:
      return -1
    return binary_search(arr[center_index + 1:], target, center_index + index + 1)
  else:
    # ターゲットが真ん中の値より小さい場合は、真ん中より左側の部分配列を再帰的に探索
    return binary_search(arr[:center_index], target)

def binary_search_copilot(arr, target):
  if len(arr) == 0:
    return -1
  mid = len(arr) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search_copilot(arr[:mid], target)
  else:
    result = binary_search_copilot(arr[mid + 1:], target)
    return -1 if result == -1 else mid + 1 + result

print(binary_search([2, 3, 4, 5, 6], 4)) # 2
print(binary_search_copilot([2, 3, 4, 5, 6], 4)) # 2