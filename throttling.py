def throttlinggateway(requesttime):
    reqcounter = 0
    timeset = 0
    dropped = 0
    reqdict = {}
    for element in requesttime:
        if element not in reqdict and element - timeset < 9 and reqcounter < 20:
            reqdict[element] = 1
            reqcounter += 1
        elif (
            element in reqdict
            and reqdict[element] < 3
            and element - timeset < 9
            and reqcounter < 20
        ):
            reqdict[element] += 1
            reqcounter += 1
            if element - timeset > 10:
                timeset += 10
        else:
            dropped += 1
            if reqcounter > 20 and timeset > 60:
                reqcounter = 0
    return dropped


if __name__ == "__main__":
    requesttime = [
        1,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        3,
        4,
        4,
        4,
        5,
        5,
        5,
        6,
        6,
        6,
        7,
        7,
        7,
        7,
        11,
        11,
        11,
        11,
    ]
    print(throttlinggateway(requesttime))
