# fname = input("Enter file name: ")
def readwordstolist():
    fh = open("romeo.txt")
    lst = list()
    for line in fh:
        word = line.rstrip().split()
        for element in word:
            if element in lst:
                continue
            else:
                lst.append(element)


def emaillist():
    # fname = input("Enter file name: ")
    # if len(fname) < 1 : fname = "mbox-short.txt"
    email = list()
    fh = open("mbox-short.txt")
    count = 0
    for line in fh:
        line.rstrip()
        if not (line.startswith("From ")):
            continue
        words = line.split()
        email.append(words[1])
        count = count + 1
    print(email)
    print("There were", count, "lines in the file with From as the first word")


if __name__ == "__main__":
    emaillist()
