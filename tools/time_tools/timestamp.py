# !/usr/bin/python3
import datetime
import sys

def main(argv):
    un_time = int(argv[0])
    times = datetime.datetime.fromtimestamp(un_time)
    print(times)

if __name__ == "__main__":
    main(sys.argv[1:])
