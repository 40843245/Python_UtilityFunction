# Release Notes
## In version 1
### Release Date:
2023/02/20 22:16 p.m.
### What can we do?
One can perform in the zip file.
1. For LetterHandler_class.py, one can insert specificied string named inserted_string into 

specificied string named target_string for each list which is splitted by the delimiter with specificied string as input at begin and at end.

Also, you can determine to strip extra specificied inserted_string if exists by the parameter.

2. For PythonCMDRunner_class.py and PythonCMDRunner_class.py given a file name, generate the cmd for executing DOS prompt, executing it in DOS prompt.

Someone may think the redundency of my code.

To do 1, why don't I write two functions or methods. One for insert at the begin while another one at the end.

The reason may amaze you.

Simply said, I will use it with other purpose in future.

If I write two functions .I have to copy and paste it.

However, I won't want to do this since the following reasons.

1) Although I think it takes me less time to copy and paste, it is NOT easier to maintain and extend my code.

When I want to extend, I have to start to write my new function ( and I will write lots of statements).

When I want to maintain, I have to modify it two times instead of once.

It is the reason why I write a method named Transfrom_AtMultiLine which required a function as its parameter.

## In version 2
### Release Date:
2023/03/24 21:32 p.m.

### Added
Added a new .zip file named "DOScmd_taskmgr.zip" which contains two python files.

1) taskmgr_class.py
2) DOScmd_Runner_class.py (main file)

Installing and unzip the file then execute DOScmd_Runner_class.py with Python. 

Then you will see the task manager is opened.



