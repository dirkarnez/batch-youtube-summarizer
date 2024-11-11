@echo off
set PYTHON_DIR=D:\Softwares\python-3.10.8-amd64-portable
set PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts

:end
cls &&^
set /p id="Enter video id: "
python main.py --video-id="%id%" &&^
pause &&^
goto end

pause