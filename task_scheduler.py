"""Task Scheduler - Schedule tasks with minimum idle time."""
from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """least_interval function."""
    interval = "idle"
    task_list = []
    idle_period = 0
    task_types = {}
    for task in tasks:
        if task not in task_types:
            task_types[task] = 1
        else:
            task_types[task] += 1
    if n != 0:
        idle_period = len(tasks) / n
    new_length = (len(tasks)) + n
    k = 0
    print(n)
    for i in range(0, new_length):
        if i % idle_period == 0 and i != 0 and n != 0:
            task_list.append(interval)
        else:
            if k < len(tasks):
                task_list.append(tasks[k])
                k += 1
    return len(task_list)


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    # print(least_interval(tasks, n))
