"""def recursive_fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

#calling the function in main
n = print("Enter a number:")
#summation = recursive_fibonacci(n)
print("Summation of Fibonacci series:")
i=0
for i in range(n):
    print(recursive_fibonacci(i)),"""


def fibonacci(n):
    """fibonacci function."""
    if n <= 1:
        return n
    x = fibonacci(n - 1) + fibonacci(n - 2)
    return x


""" for i in range(n):
    print(fibonacci(n)) """


def fib_dynamic_top_down(n):
    """fib_dynamic_top_down function."""
    if n in range(0, 1):
        return 1
    """ fib_dynamic_top_down(0)=1
    fib_dynamic_top_down(1)=1 """
    for i in range(2, n):
        # fib_dynamic_top_down(n) = fib_dynamic_top_down(n-2)+fib_dynamic_top_down(n-1)
        return int(fib_dynamic_top_down(i - 2) + fib_dynamic_top_down(i - 1))


n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
# n1 = fib_dynamic_top_down(n)
for i in range(0, n):
    print(fib_dynamic_top_down(n))
