import sys
import math
import subprocess

#Outputs the test
def test():
    result = subprocess.call(sys.argv[1:], shell=True)
    print(result)


if __name__ == "__main__":
    test() 
