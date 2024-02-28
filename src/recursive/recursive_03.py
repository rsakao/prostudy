# 問題3: 文字列の反転
# 与えられた文字列を反転させる再帰関数を書いてください。

def reverse_string(str):
  if len(str) == 0:
    return str
  return reverse_string(str[1:]) + str[0]
