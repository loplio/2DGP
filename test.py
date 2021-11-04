unsort_list = [1, 7, 4, 3, 8, 9, 5, 2, 6]


def bubble_sort(list_):
    pass


def selection_sort(list_):
    for i in range(0, len(list_)):
        min_ = list_[i]
        buffer = i
        for j in range(i, len(list_)):
            if min_ > list_[j]:
                min_ = list_[j]
                buffer = j
        if list_[i] > min_:
            list_[buffer] = list_[i]
            list_[i] = min_


def insert_sort(list_):
    for i in range(0, len(list_)):
        min_ = list_[i]
        buffer = i
        for j in range(0, buffer):
            pass
    pass


def shell_sort(list_):
    pass


# bubble_sort(unsort_list)
selection_sort(unsort_list)
print(unsort_list)