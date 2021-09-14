#!/usr/bin/env python

def dcp(list, number):

    list.sort()
    if sum(list[::2]) <+ number:
        return True
    return False

def main():
    test = [10, 15, 3, 7]
    print(dcp(test, 17))

if __name__ == "__main__":
    main()
