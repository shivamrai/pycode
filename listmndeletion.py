#listmndeletion
def deletionmn(soln):
    m,n = 2,3
    numm,numn = 0,0
    k=0
    while(k<len(soln)):
        if(numm<m):
            numm+=1
            k+=1
        elif(numm==m):
            numm=0
            numn = n
            while(numn!=0):
                if(k<len(soln)):
                    listA.pop(k)
                numn-=1
            k+=1
        
    print(soln)

if __name__ == "__main__":
    listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,20]
    deletionmn(listA)