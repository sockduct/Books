
ECHO OFF
CLS
:MENU
ECHO.
ECHO ---THIS IS USED TO INSTALL PYTHON PACKAGES----
ECHO ---FIRST ADD TO YOUR PATH TO "C:\Python27\;C:\Python27\scripts\;"---
ECHO.
ECHO ECHO """"FIRST CHANGE YOUR PATH MANUALLY THEN RUN ANY SCRIPT BELOW""""
ECHO.
ECHO ...............................................
ECHO Select The Number of the Task You Wish To Run.
ECHO ...............................................
ECHO.
ECHO 1 - Install Distrubite -- MUST BE DONE FIRST
ECHO 2 - Install Beautiful Soup 4
ECHO 3 - Install DNS Python
ECHO 4 - EXIT
ECHO.
SET /P M=Enter The Number You Want To Execute then press ENTER:
IF %M%==1 GOTO INSTALLDISTR
IF %M%==2 GOTO INSTALLBEAUTSOUP
IF %M%==3 GOTO DNSPYTHON
IF %M%==4 GOTO EOF

:INSTALLDISTR
cls
python "C:\Documents and Settings\civuser\desktop\distribute_setup.py"
PAUSE
cls
GOTO MENU

:INSTALLBEAUTSOUP
easy_install beautifulsoup4
PAUSE
cls
GOTO MENU

:DNSPYTHON
easy_install dnspython
PAUSE
cls
GOTO MENU

:DNSPYTHON
easy_install dnspython
PAUSE
cls
GOTO MENU

