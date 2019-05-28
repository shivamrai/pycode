def justmatrix(n):
    for i in range(0,n):
        for j in range(0,i-1):
            print(" ")
        for j in range(i,n):
            print("# ",end="")            
        print("\r")

justmatrix(3)