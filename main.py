#!/usr/bin/python3
"""
Find sum of 2 numbers to match a given number
"""


import random
MAX = 100
SAMPLE_SIZE = 5


def main():
    """
    main driver program
    """
    the_list = (random.sample(range(MAX), SAMPLE_SIZE) +
                random.sample(range(MAX), SAMPLE_SIZE))
    the_num = random.randint(1, MAX)
    print(the_list, the_num)

    print(any(the_num - item in the_list[n+1:]
              for n, item in enumerate(the_list)))

    for i in the_list:
        val = the_num - i
        count = the_list.count(val)
        if count > 1 or (count and val != i):
            print("True ", the_num - i, i)
            break
    else:
        print("False")


if __name__ == "__main__":
    main()
