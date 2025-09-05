@echo off
set PYTHON_DIR=D:\Softwares\python-3.10.8-amd64-portable
set PATH=%PYTHON_DIR%;%PYTHON_DIR%\Scripts

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

:end
cls &&^
set /p id="Enter video id: "
python main.py --video-id="%id%" &&^
pause &&^
goto end

pause