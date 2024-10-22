@echo off

start "Backend Server" powershell -NoProfile -Command ^
  "Start-Process powershell -ArgumentList '-NoProfile -NoExit -Command cd E:\django; Set-ExecutionPolicy RemoteSigned -Force; .\venv\Scripts\activate; cd E:\django\backend; python manage.py runserver' -Verb RunAs"

start "Frontend Dev" powershell -NoProfile -Command ^
  "Start-Process powershell -ArgumentList '-NoProfile -NoExit -Command cd E:\django; Set-ExecutionPolicy RemoteSigned -Force; .\venv\Scripts\activate; cd E:\django\frontend; npm run dev' -Verb RunAs"
