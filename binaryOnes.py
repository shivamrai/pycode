def oneCounter(n):
    arrayList = []
    bool = n%2
    print(bool)
    while(n<2):
        print(n%2)
        n = n%2
        arrayList.append(n)
    print(arrayList)

if __name__ == "__main__":
    oneCounter(13)