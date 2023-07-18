@echo off

set NewUserName=NewUser

:: Create a new user
net user %NewUserName% /add

:: Add the new user to the administrators group
net localgroup administrators %NewUserName% /add

:: Restart the computer
shutdown /r /t 0
