# !/usr/bin/python3
import datetime
import sys


def main(argv):
    print(argv)
    time_stamp = datetime.datetime.timestamp(datetime.datetime.strptime(argv[0],"%Y-%m-%d %H:%M:%S"))
    print(time_stamp)


if __name__ == "__main__":
    main(sys.argv[1:])
