Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' 启动wsgi.py进程
objShell.Run "python D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\backend\wsgi.py", 0, False

' 等待一段时间，确保wsgi.py进程已经启动
WScript.Sleep 5000

' 启动nginx进程

' objShell.Run "D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\nginx", 0, False  ' 在Windows系统中，可执行文件exe的扩展名通常是可选
objShell.Run "D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\nginx.exe", 0, False

' 打开网页
objShell.Run "msedge http://localhost:8088/", 0, True

' 释放objShell对象
Set objShell = Nothing