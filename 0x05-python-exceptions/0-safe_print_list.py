#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cntr = 0
    for i in my_list:
        if cntr < x:
            try:
                print("{}".format(my_list[cntr]), end='')
            except IndexError:
                break
            else:
                cntr += 1
    print()
    return (cntr)
