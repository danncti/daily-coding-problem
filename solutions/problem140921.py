#!/usr/bin/env python

def dcp(lst, number):

    if len(lst)>=2:
        for value in lst[1::]:
            if lst[0] + value == number:
                return True
        dcp(lst[1::], number)
    return False

def main():

    assert not dcp([], 17)
    assert not dcp([4], 17)
    assert dcp([17, 0], 17)
    assert dcp([10, 15, 3, 7], 17)

if __name__ == "__main__":
    main()
