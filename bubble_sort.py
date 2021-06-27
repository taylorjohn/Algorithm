# Bubble Sort

import random


def generate_random_list(n):
    # insert code here
    # should return a list containing n random elements
    my_list = []
    for i in range(n):
        my_list.append(random.randint(-4*n, 4*n))
    return my_list

def bubble_sort(my_list):
    # insert sorting code here
    for i in range(len(my_list), 1, -1):
        for j in range(1, i):
            if my_list[j-1] > my_list[j]:
                my_list[j-1], my_list[j] = my_list[j], my_list[j-1]


def main():
    my_list = generate_random_list(20)
    print(my_list)
    bubble_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()
