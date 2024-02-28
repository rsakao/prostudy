# 再帰関数のサンプル
# 階上計算
def factorial(n):
  """
  Calculate the factorial of a number.

  Parameters:
  n (int): The number for which factorial is to be calculated.

  Returns:
  int: The factorial of the given number.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(5)) # 120