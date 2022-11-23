# Basic-Security-Device

## What the program does?

The program takes a string of any length and using a finite state machine checks if you enter the correct sequence of digits (0-9) to unlock/lock the program.

## How to build and run executable

Since this is a Python program you can but don't need to build it. You only need to execute it which is done in Windows 11 by going to the git clone folder that you made -> entering the folder "Python" -> right click in the folder -> open in terminal (should look like ...\Basic-Security-Device\Python) -> type "python device.py" you can also open terminal in the main folder and type "python Python/device.py". This is also assuming you already have python installed if not this program was made from [python 3.10.6](https://www.python.org/downloads/release/python-3106/)

## Tested On

This program has been run on and tested on thoroughly in Windows 11. It has not been tested on any other platform.

## Unit testing

to run unit testing and coverage on windows 11 you need to go to the git clone folder that you made -> enter the folder "Python" -> right click in folder -> open in terminal (should look like ...\Basic-Security-Device\Python) -> type "pip install coverage" -> type "coverage run -m unittest discover" -> type "coverage report -m". This is also assuming you have Python already installed if you install it.

## Other files

The other files that can be found in the folder "Python" are "data.txt", "data_getter", "device_random.py", "raw_data.txt", and the unit test file. 

* data.txt - text file consisting of a random guesser trying to get in and its average number of tries, its min number of tries, and its max number of tries.
* data_getter - a python program that take the raw_data.txt file and does math to then output into the data.txt
* device_random.py - python program very similar to "device.py" however this in this version if you enter a blank string then it tries to brunt force the security by throwing random strings at it until it break through where it then sends the count to a new line in raw_data.txt
* raw_data.txt - a long list of numbers that are the amount of tries it took the random guesser to get through the security. The present file consists of nearly 50,000 attempts.

## Other

Author: Alan P Prymon 

licensing: The Unlicense
