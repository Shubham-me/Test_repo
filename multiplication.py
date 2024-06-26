from addition.py import add
def multiply(a,b):
  res = 0
  for i in range(b):
    res = add(res,a)
  return res
