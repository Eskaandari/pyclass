#barnamei baraye be dast avardane jomleye n Fibonacci
def Fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return 1
    for i in range(2,n + 1):
        c = a + b
        a = b
        b = c
    return c
natije_Fibonacci = Fibonacci(int(input("adad ra vared konid:\n")))
print(natije_Fibonacci)
