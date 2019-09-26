import random


def main():
    the_list = random.sample(range(100), 10)
    the_num = random.randint(1, 100)
    print(the_list, the_num)

    print(any(the_num - item in the_list for item in the_list))

    for i in the_list:
        if the_num - i in the_list:
            print("True ", the_num - i, i)
            break
    else:
        print("False")


if __name__ == "__main__":
    main()
