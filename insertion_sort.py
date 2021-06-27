# Insertion Sort

import random

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                break

def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # this call to random.shuffle will make it in random order
    random.shuffle(my_list)
    insertion_sort(my_list)
    print(my_list)


if __name__ == "__main__":
    main()
