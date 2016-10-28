@echo off
echo Batch script // Upload to Unixpool via Putty SCP
setlocal enabledelayedexpansion
:: Made by Patrick Abraham

:: Replace with path to the filefolder
:: Example path_to_filefolder=C:\Users\Nyancat\CoMa_I_Pa\

set path_to_filefolder= Replace

:: Replace with path to pscp.exe (Downloadable via http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
:: Example path_to_pscpfolder=C:\putty\

set path_to_pscp= Replace



:: Here starts the path to hell.



if exist %path_to_pscp%pscp.exe (
echo Enter Account
echo   Example co1-000
set /P acc=: 
echo.
echo Enter Filename:
echo   Example PA01 [for PA01.py]
set /P obj=: 
echo.

if exist %path_to_filefolder%!obj!.py (

%path_to_pscp%pscp.exe %path_to_filefolder%!obj!.py !acc!@unixpool.math.tu-berlin.de:./!obj!.py

) else (echo. & echo !obj!.py does not exist in the folder %path_to_filefolder% ! & echo.)
) else (echo. & echo Pscp doesn't exist at %path_to_pscp%! & echo.)
pause