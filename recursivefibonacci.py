def fibonacci(n):
    """fibonacci function."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_dynamic_top_down(n):
    """fib_dynamic_top_down function."""
    if n in range(0, 1):
        return 1
    for i in range(2, n):
        # fib_dynamic_top_down(n) = fib_dynamic_top_down(n-2)+fib_dynamic_top_down(n-1)
        return int(fib_dynamic_top_down(i - 2) + fib_dynamic_top_down(i - 1))
    return 0


n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for _ in range(0, n):
    print(fib_dynamic_top_down(n))
