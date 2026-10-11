from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_student():
    conn = get_db_connection()
    std_id = request.form['student_ID']
    std_name = request.form['student_Name']
    major = request.form['Major']
    score = request.form['Score']
    grade = request.form['Grade']

    conn.execute('''
        INSERT INTO student_table (ID, Name, Major, Score, Grade)
        VALUES (?, ?, ?, ?, ?)
        ''', (std_id, std_name, major, score, grade))

    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
    search_query = ''
    conn = get_db_connection()
    if  request.method == "POST":
        search_query = request.form.get('search', '').strip()
        query ="SELECT * FROM student_table WHERE Name LIKE ?"
        students = conn.execute(query,('%' + search_query + '%',)).fetchall()

        add_student()
    else:
        students = conn.execute('SELECT * FROM student_table').fetchall()

    conn.close()
    # students = [
    #     {"id" : 1, "Name": "Alice"},
    #     {"id" : 2, "Name": "Bob"},
    #     {"id" : 3, "Name": "Charlie"},
    #     {"id" : 4, "Name": "Diana"},
    #     {"id" : 5, "Name": "Kevin"},
    #     {"id" : 6, "Name": "Johnson"}
    # ]

    # examResult = [
    #         {"Name" : "Alice", "Mark": "A"},
    #         {"Name" : "Bob", "Mark": "A"},
    #         {"Name" : "Charlie", "Mark": "B"},
    #         {"Name" : "Diana", "Mark": "A"},
    #         {"Name" : "Kevin", "Mark": "A"},
    #         {"Name" : "Johnson", "Mark": "B"}
    #     ]



    return render_template('index.html', student_list=students)

if __name__ == '__main__':
    app.run(debug=True)