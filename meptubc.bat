@echo off
echo More Easy Pscp script for TU Berlin CoMa
setlocal enabledelayedexpansion
:: Made by Patrick "Synchen" A.

:: Replace with path to the filefolder
:: Example path_to_filefolder=C:\Users\Nyancat\CoMa_I_Pa\

set path_to_filefolder= Replace


:: Replace with path to pscp.exe (Downloadable via http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
:: Example path_to_pscpfolder=C:\putty\

set path_to_pscp= Replace


:: Here starts the path to hell
:: DO NOT CHANGE ANYTHING BENEATH THIS LINE

if not %path_to_filefolder:~-1% == \	set path_to_filefolder=!path_to_filefolder!\
if not %path_to_pscp:~-1% == \			set path_to_filefolder=!path_to_pscp!\

if exist !path_to_pscp!pscp.exe (
echo Enter Account
echo   Example co1-000
set /P acc=: 
echo.
echo Enter Filename:
echo   Example PA01 [for PA01.py]
set /P obj=: 
if !obj:~-3! == .py set obj=!obj:~,-3!
echo.

if exist !path_to_filefolder!!obj!.py (

!path_to_pscp!pscp.exe !path_to_filefolder!!obj!.py !acc!@unixpool.math.tu-berlin.de:./!obj!.py

) else (echo. & echo ERROR !obj!.py does not exist in the folder !path_to_filefolder! ! & echo.)
) else (echo. & echo ERROR Pscp doesn't exist at !path_to_pscp! ! & echo.)
pause
