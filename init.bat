@echo off

python -m venv venv
call venv\Scripts\activate.bat

pip install kivy==2.3.1

python main.py
