""" def recursiveFibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return recursiveFibonacci(n-1)+recursiveFibonacci(n-2)

#calling the function in main
n = print("Enter a number:")
#summation = recursiveFibonacci(n)
print("Summation of Fibonacci series:")
i=0
for i in range(n):
    print(recursiveFibonacci(i)), """

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        x=fibonacci(n-1) + fibonacci(n-2)
        return(x)


""" for i in range(n):
    print(fibonacci(n)) """
def fibDynamicTopDown(n):
    if n in range(0,1):
        return 1
    """ fibDynamicTopDown(0)=1
    fibDynamicTopDown(1)=1 """
    for i in range(2,n):
        #fibDynamicTopDown(n) = fibDynamicTopDown(n-2)+fibDynamicTopDown(n-1)
        return int(fibDynamicTopDown(i-2)+fibDynamicTopDown(i-1))

n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
#n1 = fibDynamicTopDown(n)
for i in range(0,n):
    print(fibDynamicTopDown(n))
