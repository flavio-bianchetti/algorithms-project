def string2array(string):
    arr = list()
    for char in string:
        arr.append(char)
    return arr


def selection_Sort(string):
    sort_string = string2array(string)
    for index_x in range(len(sort_string) - 1):
        min_index = index_x
        for index_y in range(index_x + 1, len(sort_string)):
            if sort_string[index_y] < sort_string[min_index]:
                min_index = index_y
        aux = sort_string[index_x]
        sort_string[index_x] = sort_string[min_index]
        sort_string[min_index] = aux
    return sort_string


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    string1 = isinstance(first_string, str)
    string2 = isinstance(second_string, str)
    if not string1 or not string2:
        return False

    lower_string1 = first_string.lower()
    lower_string2 = second_string.lower()

    if selection_Sort(lower_string1) == selection_Sort(lower_string2):
        return True
    else:
        return False
