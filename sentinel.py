if __name__ == "__main__":
    # number = input('Enter a number')
    # list = [number]
    # print("Enter a number (0 to stop) ")
    # for x in iter(input,"-1"):
    #     print("Enter a number (0 to stop) ")
    #     list.append(int(x))
    # print(list)
    number = input("Enter a number")
    list = []
    while int(number) != -1:
        list.append(number)
        number = input("Enter a number")
    print(list)
