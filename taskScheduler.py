def leastInterval(self, tasks: List[str], n: int) -> int:
    interval = "idle"
    taskList = []
    idlePeriod = 0
    taskTypes = {}
    for task in tasks:
        if task not in taskTypes:
            taskTypes[task]=1
        else:
            taskTypes[task]+=1
    if(n!=0):
        idlePeriod = len(tasks)/n
    newLength = (len(tasks))+n
    k=0
    print(n)
    while(not any taskTypes.values()):
        
    for i in range(0,newLength):
        if(i%idlePeriod==0 and i!=0 and n!=0):
            taskList.append(interval)
        else:
            if(k<len(tasks)):
                taskList.append(tasks[k])
                k+=1
    return len(taskList)

if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"] 
    n = 2
    print(leastInterval(tasks,n)
    