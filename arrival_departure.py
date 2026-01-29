"""Platform for Trains - Find minimum platforms needed."""


def arrival_dep(arr_input, dep_input):
    """arrival_dep function."""
    dict1 = {}
    for i in range(0, len(arr_input) - 1):
        dict1[arr_input[i]] = "arr"
    for i in range(0, len(dep_input) - 1):
        dict1[dep_input[i]] = "dep"
        # dict1.keys()
        sorted(dict1)

    max_platforms = 0
    for _, v in dict1.items():
        if v == "arr":
            max_platforms += 1

    print(dict1)


if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    arr.sort()
    dep.sort()
    arrival_dep(arr, dep)
