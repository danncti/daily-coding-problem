#!/usr/bin/env python3

def dcp(lst):
    i = 0
    new_list = []
    lst_len = len(lst)

    while i < lst_len:
        new_value = 1
        ii = 0
        while ii < lst_len:
            if i != ii:
                new_value *= lst[ii]
            ii += 1
        new_list.append(new_value)
        i += 1
    return new_list


def main():

    assert dcp([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert dcp([3, 2, 1]) == [2, 3, 6]

if __name__ == "__main__":
    main()
