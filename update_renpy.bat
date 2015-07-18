rem  set RENPY=/path/to/renpy
rem  set DRACYKEITON=/path/to/dracykeiton
rem  set HIREDGUNS=/path/to/hiredguns

cd %DRACYKEITON%
git pull
xcopy dracykeiton %RENPY%\lib\pythonlib2.7\dracykeiton /Y
cd %HIREDGUNS%
git pull
xcopy core/hiredguns %RENPY%\lib\pythonlib2.7\hiredguns /Y
