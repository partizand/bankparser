@echo off

call ".pycharmrc.bat"

set bankfile=statement.csv
set bank=vtb24
set downloadsdir=c:\Users\���짮��⥫�\Downloads\
set curdir=%~dp0


move %downloadsdir%%bankfile% %curdir%%bankfile%
bankparser convert %bank% %curdir%%bankfile%
pause
