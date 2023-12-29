Complete recreation of Return-To-Libc attack on created executable file ret2libc

The vulnerable executable acts as a simple mad libs taking in a string input and outputting to a file called pizza.txt

Exploit python file attack.py runs ret2libc executable and sends paylaod as input

gadgets.txt shows the list of all available gadgets in ret2libc2 which can be used in the return oriented programming attack

ret2libc2, ret2libcASLR, ret2libcCFI are variations of the ret2libc executable with different defense methods enabled

attackASLR.py is the attack exploit file used for the ret2libcASLR executable

gadgetsASLR.txt contains the gadgets for the ret2libcASLR file
