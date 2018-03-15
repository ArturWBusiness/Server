@ECHO OFF
:loop
cls
SET /P number=Enter number of the task to execute: 
cls
python "Task %number%.py"
GOTO loop
