def factorialfinder(n):
    if n == 0:
        return 1
    else:
        print("On Recursive step the value is " + str(n))
        return n * factorialfinder(n - 1)


print(factorialfinder(6))
