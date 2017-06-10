import os
import subprocess

def foo():
	subprocess.call("./shell_test.sh", shell=True)
	pass


if __name__ == '__main__':
	foo()