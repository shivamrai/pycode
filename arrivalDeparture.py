def arrivalDep(arr, dep):
    dict1 = {}
    for i in range(0, len(arr)-1):
        dict1[arr[i]] = 'arr'
    for i in range(0, len(dep)-1):
        dict1[dep[i]] = 'dep'
    #dict1.keys()
        sorted(dict1)

    maxPlatforms = 0
    for k,v in dict1.items():
        if(v=='arr'):
            
    print(dict1)

if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800] 
    dep = [910, 1200, 1120, 1130, 1900, 2000] 
    arr.sort()
    dep.sort()
    arrivalDep(arr,dep)