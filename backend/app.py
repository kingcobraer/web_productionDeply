from flask import Flask, jsonify, request
import sqlite3

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_all_student_scores():
    # conn = sqlite3.connect('./database/student.db')  # 实测,开发环境必可用相对路径也可用绝对路径
    conn = sqlite3.connect(r"D:\Files_Nas_PC\IT_Learning\HTML_CSS_JS\WebSever\nginx-1.24.0\productionDeply\backend\database\student.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    # print(results)
    conn.close()
    return results

def add_student_score(name, english, math, chinese):
    conn = sqlite3.connect('./database/student.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, english, math, chinese) VALUES (?, ?, ?, ?)",
                   (name, english, math, chinese))
    conn.commit()
    conn.close()

def update_student_score(name, english, math, chinese):
    conn = sqlite3.connect('./database/student.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET english=?, math=?, chinese=? WHERE name=?",
                   (english, math, chinese, name))
    conn.commit()
    conn.close()

def delete_student_score(name):
    conn = sqlite3.connect('./database/student.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name=?", (name,))
    conn.commit()
    conn.close()

@app.route('/api/getStudentScores', methods=['GET'])
def api_get_student_scores():
    results = get_all_student_scores()
    students = []
    for result in results:
        students.append({
            'name': result[1],
            'english': result[2],
            'math': result[3],
            'chinese': result[4]
        })
    return jsonify(students)

@app.route('/api/addStudentScore', methods=['POST'])
def api_add_student_score():
    
    data = request.get_json()
    data = data['_value']      # 组合式API写法,必须加这一句!!  选项式不可加. 原因不知.
    
    #data = request.get_json()['_value']   # 将上面两句合并成一句, 实测可行! 也是标准的简化写法

    # print('这是data数据>>>>>>>>>',data)

    name = data['name']
    english = data['english']
    math = data['math']
    chinese = data['chinese']
    add_student_score(name, english, math, chinese)
    return jsonify({'message': 'Student score added successfully'})

@app.route('/api/updateStudentScore', methods=['PUT'])
def api_update_student_score():
    data = request.get_json()
    name = data['name']
    english = data['english']
    math = data['math']
    chinese = data['chinese']
    update_student_score(name, english, math, chinese)
    return jsonify({'message': 'Student score updated successfully'})

@app.route('/api/deleteStudentScore', methods=['DELETE'])
def api_delete_student_score():
    data = request.get_json()
    name = data['name']
    delete_student_score(name)
    return jsonify({'message': 'Student score deleted successfully'})

if __name__ == '__main__':
    app.run()
