def listsplice(passedlist):
    total = 0
    for i in range(0, len(passedlist)):
        total = total + passedlist[i]
    if total % 3 == 0:
        return 1
    else:
        return 0
