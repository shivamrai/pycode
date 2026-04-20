from collections import Counter, defaultdict


if __name__ == "__main__":
    test_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(test_arr)
    res = defaultdict(list)
    for i in range(len(test_arr)):
        if test_arr[i] not in res:
            res[tuple(Counter(test_arr[i]).items())].append(test_arr[i])

    for word in test_arr:
        # Sort the Counter items so anagrams produce the exact same tuple
        key = tuple(sorted(Counter(word).items()))
        res[key].append(word)

    for k, v in res.items():
        print(k, " ", v)
