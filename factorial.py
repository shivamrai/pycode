def factorialfinder(n):
    if(n==0):
        return 1
    else:
        return n*factorialfinder(n-1)

print(factorialfinder(6))