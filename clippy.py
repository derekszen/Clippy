"""
Prints you a clippy using the input text you give it
"""

import sys
import math
import subprocess
import random

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
|
/
"""

angry_clippy = r"""
                    _.-;:q=._
                  .' j=""^k;:\.
                 ; .F       ";`Y
                ,;.J_        ;'j
              ,-;"^7F       : .F           _________________
             ,-'-_<.        ;gj. _.,---""''               .'
            ;  _,._`\.     : `T"5,                       ;
            : `?8w7 `J  ,-'" -^q. `                     ;
             \;._ _,=' ;   n58L Y.                     .'
               F;";  .' k_ `^'  j'                     ;
               J;:: ;     "y:-='                      ;
                L;;==      |:;   jT\                  ;
                L;:;J      J:L  7:;'       _         ;
                I;|:.L     |:k J:.' ,  '       .     ;
                |;J:.|     ;.I F.:      .           :
               ;J;:L::     |.| |.J  , '   `    ;    ;
             .' J:`J.`.    :.J |. L .    ;         ;
            ;    L :k:`._ ,',j J; |  ` ,        ; ;
          .'     I :`=.:."_".'  L J             `.'
        .'       |.:  `"-=-'    |.J              ;
    _.-'         `: :           ;:;           _ ;
_.-'"             J: :         /.;'       ;    ;
='_ k;.. _.;:Y' , .' "---..__Y;."-=';:=' , .' ""
"""

first_box = r"""
      _
     /
     |
     |
     |
  <--|
     |
     |
     \_
"""


def process_Command(command):
    command_List = command.split()
    result = subprocess.call(command_List[1:], shell = True)
    return result

def print_Clippy(message):
    clippy = clippy.split("\n")
    first_box = first_box.split("\n")
    end_box = end_box.split("\n")
    length_of_line = 0
    words_per_line = 30
    message_list = message.split()
    #so there is enough space
    #print words_per_line, length_of_line
    usedwords = 0
    for line in xrange(len(first_box)):
        if ((line != len(first_box)-2 and line >= 3) ):
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
    for line in xrange(len(first_box)):
        if (line == 2) or (line == len(first_box)-2):
            spacer = "_"
        else:
            spacer = " "
        #Prints spacing, to prevent the text from appearing at the top.
        if (line < len(first_box)/3) or (line == len(first_box)-2):
            s = clippy[line] + " " + first_box[line] + ((length_of_line * spacer) + end_box[line])
            print s
        #Prints words
        elif line >= len(first_box)/3:
            output = []
            output.append(clippy[line] + " ")
            output.append(first_box[line])

            current_words = 0
            tempstr = 0

            while (current_words < words_per_line) and (len(message_list) > 0):
                this_word = (message_list).pop(0)
                output.append(this_word + " ")
                #output.append((length_of_line - len(this_word) ) * " ")
                current_words += 1
                tempstr += len(this_word)+1
            output.append((length_of_line - tempstr) * " ")
            output.append(end_box[line])
            print "".join(output)

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
