import sys
import math
import subprocess

#Outputs the test
def test():
    subprocess.call(sys.argv[1:], shell=True)

list1 = [1,2,3,4,5]

if __name__ == "__main__":
	print(len(list1))
	for x in xrange(len(list1)):
		print(x)
