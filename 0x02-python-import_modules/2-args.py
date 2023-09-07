#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argc - 1))
        while i < argc:
            print("{:d}: {}".format(i, sys.argv[i]))
            i += 1
