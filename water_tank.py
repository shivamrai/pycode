"""Water Tank - Calculate water trapped."""


def max_area(height_arr) -> int:
    """max_area function."""
    # area_max = -32768
    # area = 0
    # for i in range(0,len(height_arr)-1):
    #     for j in range(0,i):
    #         area = height_arr[i]*height_arr[j]
    #         if(area>area_max):
    #             area_max = area
    # return area_max
    maxarea = -32767
    area = 0
    if len(height_arr) == 2:
        area = height_arr[0] * height_arr[1]
        return area
    list_length = int(len(height_arr) - 1)
    for i in range(0, list_length - 1):
        for j in range(len(height_arr) - 1, i, -1):
            area = min(height_arr[i], height_arr[j]) * (j - i)
            maxarea = max(maxarea, area)
    return maxarea


if __name__ == "__main__":
    height_input = [1, 1]
    print(max_area(height_input))
