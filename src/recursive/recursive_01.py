# 問題1: フィボナッチ数列
# フィボナッチ数列の第 n 項を返す再帰関数を書いてください。フィボナッチ数列は、次のように定義されます：

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) (n > 1 の場合)

def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

# この再帰関数は、n が大きくなると計算量が指数的に増加するため、効率が悪いです。そのため、以下のような非再帰関数を使うことが一般的です：
def fibonacci_copilot(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a
