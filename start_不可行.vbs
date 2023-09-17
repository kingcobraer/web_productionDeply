Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' 启动waitress.py进程
objShell.Run "python D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\backend\server_waitress.py", 0, False

' 等待一段时间，确保.py进程已经启动
WScript.Sleep 5000

' 启动nginx进程
objShell.Run "D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\nginx.exe", 0, False

WScript.Sleep 5000

' 关闭nginx进程
objShell.Run "cmd /c cd /d D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply && .\nginx.exe -s quit", 0, False

' 打开网页
objShell.Run "msedge http://localhost:8088/", 0, True

' 释放objShell对象
Set objShell = Nothing