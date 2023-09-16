Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' 关闭wsgi.py进程
objShell.Run "taskkill /IM python.exe /F", 0, True

' 关闭nginx进程
objShell.Run "taskkill /IM nginx.exe /F", 0, True

' 释放objShell对象
Set objShell = Nothing
