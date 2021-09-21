#!/usr/bin/env python3
###
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.


def dcp(lst):


    # remove negatives numbers
    lst = rem_negs(lst)
    print (lst)
    # remove duplicates numbers
    lst = list(set(lst))
    print(lst)

    lst.sort()

    last_item = 0
    for item in lst:

        if item == last_item :
            print("a wynik " + str(last_item))
            return last_item

        last_item +=1

        if item > last_item:
            print("b wynik " +str(last_item ))
            return last_item

        print(item)
    print("c wynik " + str(last_item +1 ))
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

    print(dcp([3, 4, -1, 1]))
    print(dcp([1, 2, 0]))
    print(dcp([0, 2, 0]))
    print(dcp([0, 2, 2, 3, 3,2 , 5]))
    # assert dcp([3, 4, -1, 1]) == 2
    # assert dcp([1, 2, 0]) == 3

if __name__ == "__main__":
    main()
