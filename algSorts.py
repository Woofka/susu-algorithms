from random import *


def arrayGenerator(n, minimum=0, maximum=100):
    array = []
    for i in range(n):
        array.append(randint(minimum, maximum))
    return array


def bubbleSort(seq):   # O(N)..O(N^2)
    """ Сортировка пузырьком (улучшенная). Идя слева направо по массиву
     меняет местами элементы, если предыдущий больше последующего.
     В среднем асимптотика ближе к O(N^2) """
    if len(seq) <= 1:
        return seq
    right_end = len(seq) - 1
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(right_end):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                not_sorted = True
        right_end -= 1
    return seq


def shakerSort(seq):   # O(N)..O(0.5 * N^2)
    """ Шейкерная сортировка. Работает аналогично сортировке пузырьком,
     но после прохода слева направо проходит справа налево, что позволяет
     в большинстве случаев ускорить сортировку"""
    if len(seq) <= 1:
        return seq
    left_end = -1
    right_end = len(seq) - 1
    not_sorted = True
    while not_sorted:
        not_sorted = False
        left_end += 1
        for i in range(left_end, right_end):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                not_sorted = True
        if not not_sorted:
            break
        right_end -= 1
        for i in range(right_end, left_end, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                not_sorted = True
    return seq


def shellSort(seq):    # ???
    """ Сортировка Шелла. ??? """
    n = len(seq)
    d = int(n/2)
    while d > 0:
        for i in range(n-d):
            j = i
            while j >= 0 and seq[j] > seq[j + d]:
                seq[j], seq[j + d] = seq[j + d], seq[j]
                j -= 1
        d -= 1
    return seq


def combSort(seq):     # O(N * logN)..O(N^2)
    """ Сортировка расческой. Перед сортировкой пузырьком проходит по массиву
     с некоторыми шагами, чтобы избавиться от 'черепах' в конце.
     В среднем асимптотика ближе к O(N * logN)"""
    if len(seq) <= 1:
        return seq
    k = 1.2473309
    right_end = len(seq) - 1
    step = right_end - 1
    not_sorted = True
    while step > 1:
        for i in range(right_end - step):
            if seq[i] > seq[i+step]:
                seq[i], seq[i+step] = seq[i+step], seq[i]
        step = int(step / k)
    while not_sorted:
        not_sorted = False
        for i in range(right_end):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                not_sorted = True
        right_end -= 1
    return seq


def insertionSort(seq):    # O(N)..O(N^2)
    """ Сортировка вставками. В среднем асимптотика близка к O(N^2) """
    if len(seq) <= 1:
        return seq
    for j in range(1, len(seq)):
        key = seq[j]
        i = j - 1
        while i >= 0 and seq[i] > key:
            seq[i + 1] = seq[i]
            i -= 1
        seq[i+1] = key
    return seq


def binInsertionSort(seq):    # ???
    """ Сортировка бинарными вставками. ??? """
    if len(seq) <= 1:
        return seq
    for i in range(len(seq)):
        x = seq[i]
        l = 0
        r = i
        while l < r:
            m = int((l + r) / 2)
            if seq[m] <= x:
                l = m + 1
            else:
                r = m
        for j in range(i, r, -1):
            seq[j] = seq[j - 1]
        seq[r] = x
    return seq


def gnomeSort(seq):
    """ Гномья сортировка. ??? """
    if len(seq) <= 1:
        return seq
    if len(seq) == 2:
        if seq[0] > seq[1]:
            seq[0], seq[1] = seq[1], seq[0]
        return seq
    cur = 1
    nextIndx = 2
    while cur < len(seq):
        if seq[cur-1] < seq[cur]:
            cur = nextIndx
            nextIndx += 1
        else:
            seq[cur-1], seq[cur] = seq[cur], seq[cur-1]
            cur -= 1
            if cur == 0:
                cur = nextIndx
                nextIndx += 1
    return seq


def selectionSort(seq):    # ???
    """ Сортировка простым выбором. ??? """
    if len(seq) <= 1:
        return seq
    n = len(seq)
    for i in range(n - 1):
        MinValue = seq[i]
        k = i
        for j in range(i + 1, n):
            if seq[j] < MinValue:
                k = j
                MinValue = seq[j]
        seq[k] = seq[i]
        seq[i] = MinValue
    return seq


def mergeSort(seq):
    """ Сортировка слиянием """
    if len(seq) <= 1:
        return seq
    middle    = len(seq)//2
    leftHalf  = seq[:middle]
    rightHalf = seq[middle:]
    mergeSort(leftHalf)
    mergeSort(rightHalf)
    i = 0; j = 0; k = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            seq[k] = leftHalf[i]
            i += 1
        else:
            seq[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        seq[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        seq[k] = rightHalf[j]
        j += 1
        k += 1
    return seq


def quickSort(seq, leftEnd=None, rightEnd=None):
    """ Быстрая сортировка """
    if len(seq) <= 1:
        return seq
    if leftEnd is None or rightEnd is None:
        leftEnd = 0
        rightEnd = len(arr) - 1
    i = leftEnd
    j = rightEnd
    bar = seq[leftEnd]
    while i < j:
        while seq[i] < bar:
            i += 1
        while seq[j] > bar:
            j -= 1
        if i <= j:
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
            i += 1
            j -= 1
    if leftEnd < j:
        quickSort(seq, leftEnd, j)
    if i < rightEnd:
        quickSort(seq, i, rightEnd)
    return seq


"""
+ Сортировка кучами ?
"""
# ----- MAIN PROGRAM -----
if __name__ == "__main__":
    a = []
    b = [1]
    c = [1, 0]
    d = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1]
    e = [1, 0, -1, 1, 0, -1, 1, 0, -1, 1, 0, -1]
    f = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    g = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    x = arrayGenerator(10, -1000, 1000)
    y = arrayGenerator(1000, 0, 9)
    z = [a, b, c, d, e, f, g, x, y]
    test = 1
    for arr in z:
        print("Test #%d" % test)
        print("Array:                ", arr)
        print("Bubble Sort:          ", bubbleSort(arr.copy()))
        print("Shaker Sort:          ", shakerSort(arr.copy()))
        print("Shell Sort:           ", shellSort(arr.copy()))
        print("Comb Sort:            ", combSort(arr.copy()))
        print("Insertion Sort:       ", insertionSort(arr.copy()))
        print("Binary Inertion Sort: ", binInsertionSort(arr.copy()))
        print("Gnome Sort:           ", gnomeSort(arr.copy()))
        print("Selection Sort:       ", selectionSort(arr.copy()))
        print("Merge Sort:           ", mergeSort(arr.copy()))
        print("Quick Sort:           ", quickSort(arr.copy()))
        print()
        test += 1
