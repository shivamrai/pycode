if __name__ == "__main__":
    #THis program is basically a dictionary cheatsheet
    counts = dict()
    line = input('Enter a line of Text:')
    words = line.split()
    print("Words are:", words)
    print("Counting...")

    for word in words:
        counts[word] = counts.get(word,0) + 1
    print("Count of words : ", counts)

    for key in counts:
        print(key, counts[key])

    print(counts.keys())
    print(counts.values())
    print(list(counts))
    print(counts.items)
    #double iteration of a dictionary
    for keys,values in counts.items():
        print(keys,values)
    