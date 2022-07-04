def left_bin_search(sorted_seq, key):
    n = len(sorted_seq)
    left = -1
    right = n - 1                       # т.к. ответ по 'right', нужно избежать вылета за границы массива
    while right - left > 1:
        middle = (left + right) // 2    # для избежания переполнения: = left + (right - left) // 2
        if sorted_seq[middle] < key:
            left = middle
        else:
            right = middle
    # print("DEBUG | key %s | left %s | right %s" % (key, left, right))
    if 0 <= right <= n and sorted_seq[right] == key:
        print("The key '%s' is there and it's index is '%d'" % (key, right))
    else:
        print("The key '%s' isn't there" % key)


def right_bin_search(sorted_seq, key):
    n = len(sorted_seq)
    left = -1
    right = n
    while right - left > 1:
        middle = (left + right) // 2    # для избежания переполнения: = left + (right - left) // 2
        if sorted_seq[middle] <= key:
            left = middle
        else:
            right = middle
    # print("DEBUG | key %s | left %s | right %s" % (key, left, right))
    if 0 <= left <= n and sorted_seq[left] == key:
        print("The key '%s' is there and it's index is '%d'" % (key, left))
    else:
        print("The key '%s' isn't there" % key)


def left_bin_search_real(func, amount):  # исключительно для подбора ответа по какой-то монотонной функции
    left = 0
    right = amount
    while right - left > 0.1:            # указываем точность
        middle = (left + right) / 2      # для избежания переполнения: = left + (right - left) / 2
        if func(middle) == 0:            # для монотонно возрастающего графика: y = ...0,0,0,1,1,1...
            left = middle
        else:
            right = middle
    # print("DEBUG | left %s | right %s" % (left, right))
    if 0 <= right <= amount:
        print("Answer is %s" % round(right, 1))
    else:
        print("The key isn't there")


# ------ MAIN PROGRAM ------
if __name__ == "__main__":
    #    0  1  2  3  4  5  6  7  8
    a = [1, 2, 3, 4, 4, 4, 6, 9, 10]
    b = 4
    right_bin_search(a, b)
    left_bin_search(a, b)
