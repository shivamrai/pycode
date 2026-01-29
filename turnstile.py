"""Turnstile - Turnstile entry/exit tracking."""


def turnstile_times(num_customers, arr_time, direction_list):
    """turnstile_times function."""
    entry_time = []
    exit_time = []
    for i in range(0, num_customers):
        if direction_list[i] == 0:
            entry_time.append(i, arr_time[i], direction_list[i])
        else:
            exit_time.append(i, arr_time[i], direction_list[i])
    exit_time.sort()
    entry_time.sort()
    _result = [None] * num_customers
    p, q = len(entry_time), len(exit_time)
    i, j = 0, 0
    for t in range(0, 100000000):
        if i < p and j < q:
            en = entry_time.index(i)
            _ = exit_time.index(j)
            if t < en:
                pass


def compare(enter_time, exit_time, time, status):
    """compare function."""
    enter_time -= time
    exit_time -= time
    enter_time = max(enter_time, 0)
    if exit_time < 0:
        pass
    if enter_time < exit_time:
        return -1
    if enter_time == exit_time:
        if status == 1:
            return 1
        return -1
    return 1


if __name__ == "__main__":
    numCustomers = 4
    arrTime = [0, 0, 1, 5]
    direction = [0, 1, 1, 0]
    print(turnstile_times(numCustomers, arrTime, direction))
