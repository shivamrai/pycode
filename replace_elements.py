"""Replace Elements - Replace with right greatest."""


def replace_elements(arr: list) -> list:
    """replace_elements function."""
    if arr == []:
        return
    i = 0
    while i < len(arr):
        j = i
        while j < len(arr):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                arr[j] = -1
            j += 1
        i += 1
    return arr


if __name__ == "__main__":
    listA = [17, 18, 5, 4, 6, 1]
    print(replace_elements(listA))
