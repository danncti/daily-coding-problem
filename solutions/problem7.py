#!/usr/bin/env python3
import time
start_time = time.time()
def dcp(code):

    return code

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

def is_two_char(code):
    code = int(code)
    return 0 if code > 26 or code < 1 else 1

def get_message_count(code):
    print("----->", code)
    code_str = str(code)
    code_len = len(code_str)
    if code_len == 1:
        print("==1", code)
        count = 1
    elif code_len == 2:
        print("==2", code)
        count = 1 + is_two_char(code)
    else:
        print("else:::::")
        print(">2", code_str[1:])
        count = get_message_count(code_str[1:])
        print("count = ", str(count))
        print("-----" )
        if is_two_char(code_str[:2]):
            print("....>2 ", code_str[:2])
            count += get_message_count(code_str[2:])
    print("--return-----")
    return int(count)

def main():

    get_message_count("123456")

    # assert get_message_count(11) == 2
    # assert get_message_count(111) == 3
    # assert get_message_count(1111) == 5
    # assert get_message_count(1311) == 4

    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()
