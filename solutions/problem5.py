#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car( pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)

def main():

    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4

if __name__ == "__main__":
    main()
