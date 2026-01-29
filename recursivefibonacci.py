def fibonacci(num):
    """fibonacci function."""
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def fib_dynamic_top_down(num):
    """fib_dynamic_top_down function."""
    if num in range(0, 1):
        return 1
    for i in range(2, num):
        # fib_dynamic_top_down(num) = fib_dynamic_top_down(num-2)+fib_dynamic_top_down(num-1)
        return int(fib_dynamic_top_down(i - 2) + fib_dynamic_top_down(i - 1))
    return 0


n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for _ in range(0, n):
    print(fib_dynamic_top_down(n))
