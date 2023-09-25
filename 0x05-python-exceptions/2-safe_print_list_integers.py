#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cntr = 0
    for i in my_list:
        if cntr < x:
            try:
                print("{:d}".format(i), end='')
                cntr += 1
            except (ValueError, TypeError):
                pass
    print()
    return (cntr)
