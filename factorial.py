from multiplication import multiply
def factorial(n):
    res = 1
    for i in range(2,n+1):
        res = multiply(res,i)
    return res
n = 20
print(factorial(n))
