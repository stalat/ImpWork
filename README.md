## Installation

### Game requires Python-3 to be installed on host machine.
3 Core python modules are used in the script which are:
- csv
- time
- random

It implements a class which has methods defined to perform the above mentioned operations.

### Execution of file
Way to execute the file from terminal is as:
 - Navigate to folder where __learn.py__ is present
 - Use below command:
```sh
python3 learn.py
```
 -  It will ask User to enter UserName
 -  It will then ask to solve a mathematical problem
 -  User will provide his solution
 -  User will be prompted if his answer is correct or not
 -  User will be asked if he wishes to continue the Game - Y/N
 -  If User presses Y, Game will go-on
 -  If User presses N, Game will exit from
 -  If User presses any other key apart from Y/N, He will be prompted again and again to chose correct option (Y/N)
 -  When user exits the Game, He will find that there is CSV file created with name as __<user_name>.csv__. which captures - 
 -- Question
 -- User's Answer
 -- IsCorrect
 -- TimeTaken (By user to solve problem)


