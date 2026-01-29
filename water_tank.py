"""Water Tank - Calculate water trapped."""


def max_area(height) -> int:
    """max_area function."""
    # area_max = -32768
    # area = 0
    # for i in range(0,len(height)-1):
    #     for j in range(0,i):
    #         area = height[i]*height[j]
    #         if(area>area_max):
    #             area_max = area
    # return area_max
    maxarea = -32767
    area = 0
    if len(height) == 2:
        area = height[0] * height[1]
        return area
    list_length = int(len(height) - 1)
    for i in range(0, list_length - 1):
        for j in range(len(height) - 1, i, -1):
            area = min(height[i], height[j]) * (j - i)
            maxarea = max(maxarea, area)
    return maxarea


if __name__ == "__main__":
    height = [1, 1]
    print(max_area(height))
