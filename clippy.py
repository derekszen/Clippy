"""
Prints you a clippy using the input text you give it
"""

import sys
import math
import subprocess

words_list =sys.argv[1:]
length_of_input =  sum(len(x)+1 for x in words_list)
max_length = 204  #70 - width of clippy and bubble * 4
clippy = r"""
 ____
/    \
|    |
0  0
||  ||
||  ||
|\_ /|
\____/
"""

boxy = r"""
      _
     /
     |
     |
  <--|
     |
     \_
"""

post_text = r"""
\
|
|
|
|
/
"""



def main():




if __name__ = "__main__":