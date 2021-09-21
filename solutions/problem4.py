#!/usr/bin/env python3

def dcp(lst):
    # remove negatives numbers
    lst = rem_negs(lst)
    # remove duplicates
    lst = list(set(lst))

    lst.sort()

    last_item = 0
    for item in lst:

        if item == last_item :
            return last_item

        last_item +=1

        if item > last_item:
            return last_item

    return last_item +1

# remove negative number from list
def rem_negs(num_list):
    """ returns list without negative numbers and zeros """
    r = num_list[:]
    for item in num_list:
        if item < 1:
           r.remove(item)
    return r

def main():

    assert dcp([3, 4, -1, 1]) == 2
    assert dcp([1, 2, 0]) == 3
    assert dcp([0, 2, 0]) == 1
    assert dcp([0, 2, 2, 3, 3, 2, 5]) == 1

if __name__ == "__main__":
    main()
