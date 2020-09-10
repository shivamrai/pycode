
def maxArea(height) -> int:
    # area_max = -32768
    # area = 0
    # for i in range(0,len(height)-1):
    #     for j in range(0,i):
    #         area = height[i]*height[j]
    #         if(area>area_max):
    #             area_max = area
    # return area_max
    left = 0
    right = len(height)-1
    maxarea = -32767
    area = 0
    if(len(height)==2):
        area = height[0]*height[1]
        return area
    listLength = int(len(height)-1)
    for i in range(0,listLength-1):
        for j in range(len(height)-1,i,-1):
            area = min(height[i],height[j])*(j-i)
            if(area>maxarea):
                maxarea = area
    return maxarea
if __name__ == "__main__":
    height = [1,1]
    print(maxArea(height))