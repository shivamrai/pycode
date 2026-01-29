"""Apples and Oranges - Count fruits within distance ranges."""


# Complete the countApplesAndOranges function below.
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    """count_apples_and_oranges function."""
    count_of_apples = 0
    count_of_oranges = 0

    # Adjust apple positions by offset 'a' and count those in range [s, t]
    for apple_distance in apples:
        adjusted_apple = apple_distance + a
        if s <= adjusted_apple <= t:
            count_of_apples += 1

    # Adjust orange positions by offset 'b' and count those in range [s, t]
    for orange_distance in oranges:
        adjusted_orange = orange_distance + b
        if s <= adjusted_orange <= t:
            count_of_oranges += 1

    print(count_of_apples, " ", count_of_oranges)


if __name__ == "__main__":
    # st = input().split()

    s_val = 7

    t_val = 11

    # ab = input().split()

    a_val = 5

    b_val = 15

    # mn = input().split()

    m_val = 3

    n_val = 2

    apples_list = [-2, 2, 1]

    oranges_list = [5, -6]

    count_apples_and_oranges(s_val, t_val, a_val, b_val, apples_list, oranges_list)
