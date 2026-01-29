import os
from pathlib import Path


class Practice:
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    x = Practice()
    names1 = ["Amir", "Bear", "Charlton", "Daman"]
    # names2 = names1 #copy  by reference names2 and names1 point to same location
    # names3 = names1[:] #copy by value

    # names2[0] = 'Alice'
    # print(names1)
    # print(names2)
    # names3[1] = 'Bob'

    # sum = 0
    # for ls in (names1, names2, names3):
    #     if ls[0] == 'Alice':
    #         sum += 1
    #     if ls[1] == 'Bob':
    #         sum += 10

    # print(sum)#12
    # print(names1*2)
    n = 121
    a = list(map(int, str(n)))
    b = list(map(lambda x: x**3, a))
    # print(list("hello"))
    # print(if(sum(b)==n):)
    # print(os.listdir('./'))
    # read whole file into one String
    with open("rules.pro", "r") as f:
        data = f.read()
    print(data)

    # List all files in a directory using os.listdir
    basepath = "./"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            print(entry)

    # List all files in a directory using scandir()
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)

    # List all files in directory using pathlib
    basepath = Path("./")
    files_in_basepath = basepath.iterdir()
    for item in files_in_basepath:
        if item.is_file():
            print(item.name)

    # The examples below show how to get the time the files in /pycode were
    # last modified. The output is in seconds:
    with os.scandir("./") as dir_contents:
        for entry in dir_contents:
            info = entry.stat()
            print(info.st_mtime)
