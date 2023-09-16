from app import app
from waitress import serve

if __name__ == "__main__":
    #serve(app, host='0.0.0.0',port=8088) # 无法运行
    serve(app,port=8088)   # 可以运行, 访问 http://127.0.0.1:8088/api/getStudentScores