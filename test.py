import sys
import math
import subprocess

#Outputs the test
def test():
    subprocess.call(sys.argv[1:], shell=True)

if __name__ == "__main__":
	while 1:
		test()
