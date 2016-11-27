"""
Prints you a clippy using the input text you give it
"""

import sys
import math
import subprocess
import random
import signal
import os
import MEMES.py

message_list = sys.argv[1:]
length_of_input =  sum(len(x) + 1 for x in message_list)
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
|
/
"""

first_box = r"""

     /
     |
     |
  <--|
     |
     |
     \_
"""
# NAUGHTY NAUGHTY.
restrictedCommands = ["reboot", "shutdown", "fuck", "suck", "you", "rm"]


def process_Command(command):
    if (command.find("cd") != -1):
        result = os.chdir(command[1])
        return result
    for restrictedCommand in restrictedCommands:
        if (command.find(restrictedCommand) != -1):
            print(angry_clippy)
            return 1
    command_List = command.split()
    print(command_List)
    result = subprocess.call(command_List, shell = True)
    print(result)
    return result

def print_Clippy(message):
    global clippy
    global first_box
    global end_box

    clippyList = clippy.split("\n")
    first_boxList = first_box.split("\n")
    end_boxList = end_box.split("\n")
    length_of_line = 0
    words_per_line = 30
    message_list = message.split()
    #so there is enough space
    #print words_per_line, length_of_line
    usedwords = 0
    for line in xrange(len(first_boxList)):
        if ((line != len(first_boxList)-2 and line >= 3) ):
            tempstr = 0
            current_words = 0
            while ((usedwords < len(message_list) and current_words < words_per_line)):
                this_word = message_list[usedwords]
                #output.append((length_of_line - len(this_word) ) * " ")
                current_words += 1
                usedwords +=1
                tempstr += (len(this_word)+1)
                if tempstr > length_of_line:
                    length_of_line = tempstr
    for line in xrange(len(first_boxList)):
        if (line == 1) or (line == len(first_boxList)-2):
            spacer = "_"
        else:
            spacer = " "
        #Prints spacing, to prevent the text from appearing at the top.
        if (line < len(first_boxList)/3) or (line == len(first_boxList)-2):
            s = clippyList[line] + " " + first_boxList[line] + ((length_of_line * spacer) + end_boxList[line])
            print s
        #Prints words
        elif line >= len(first_boxList)/3:
            output = []
            output.append(clippyList[line] + " ")
            output.append(first_boxList[line])

            current_words = 0
            tempstr = 0

            while (current_words < words_per_line) and (len(message_list) > 0):
                this_word = (message_list).pop(0)
                output.append(this_word + " ")
                #output.append((length_of_line - len(this_word) ) * " ")
                current_words += 1
                tempstr += len(this_word)+1
            output.append((length_of_line - tempstr) * " ")
            output.append(end_boxList[line])
            print "".join(output)

def generate_Text(command):
    command_List = command.split()
    random.seed()
    commandResult = "RESULT IS AN ERROR." 
    rand_Int = random.randint(0, len(command_List)-1)
    pregenerated_Text = ["Unable to find command.", command_List[rand_Int] + " is not a real word.", \
                        "Would you like me to do this?", "This quite ineffective", \
                        "You have mispelled " + command_List[rand_Int], \
                        "Happily processing your command!", "Thank you, sir", \
                        "The following are the result of your command:\n" + commandResult, \
                        "ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR"]
    random.seed()
    rand_Int = random.randint(0, len(pregenerated_Text)-1)
    text = pregenerated_Text[rand_Int]
    return text

def trigger_warning(signal, frame):
    global angry_clippy
    print(angry_clippy)
    return 

def TRIGGERED(signal, frame):
    global nope
    print(nope[random.randint(0,len(nope)-1)])
    return 

def main():
    #Welcome message 
    print_Clippy("Hello, I'm Clippy, everyone's favorite personal assistant!")
    while 1:
        command = raw_input(">")
        process_Command(command)
        message = generate_Text(command)
        print_Clippy(message)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, trigger_warning)
    signal.signal(signal.SIGTSTP, TRIGGERED)
    main()
