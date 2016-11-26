"""
Prints you a clippy using the input text you give it
"""

import sys
import math
import subprocess
import random

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

end_box = r"""
\
|
|
|
|
/
"""

first_box = r"""
      _
     /
     |
     |
  <--|
     |
     \_
"""


def process_Command(command):
    command_List = command.split()
    result = subprocess.call(command_List, shell = True)
    return result

def print_Clippy(message):
    clippy = clippy.split("\n")
    first_box = first_box.split("\n")
    end_box = end_box.split("\n")

def generate_Text():

    random.seed()
    rand_Int = random.randint(0, sys.argv.len())
    pregenerated_Text = ["Unable to find command.", sys.argv[rand_Int] + "is not a real word."]
    rand_Int = random.randint(0, pregenerated_Text.len())
    text = pregenerated_Text[rand_Int]
    return text    

def main():
    #Welcome message 
    print_Clippy("Hello, my name is clippy, everyone's favorite personal assistant!")
    while 1:
        command = raw_input("enter your next command:")
        process_Command(command)
        message = generate_Text()
        print_Clippy(message)



if __name__ == "__main__":
    main()
