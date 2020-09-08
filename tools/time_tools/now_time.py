# !/usr/bin/python3
import datetime
import sys


def main(argv):
    now_time = datetime.datetime.now()
    now_time_stamp = datetime.datetime.timestamp(now_time)
    print(now_time, now_time_stamp)


if __name__ == "__main__":
    main(sys.argv[1:])
