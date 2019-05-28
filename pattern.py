def drawpattern(n):
    #counter = 1
    #handle spaces and then handle stars

    for i in range(0,n):
        #spaces
        for j in range(0,i+1):
            print(" ")
        #stars
        for j in range(i,n):
            print("*",end="")
        
    print("\r")

drawpattern(2)