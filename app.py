from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    students = [
        {"id" : 1, "Name": "Alice"},
        {"id" : 2, "Name": "Bob"},
        {"id" : 3, "Name": "Charlie"},
        {"id" : 4, "Name": "Diana"},
        {"id" : 5, "Name": "Kevin"},
        {"id" : 6, "Name": "Johnson"}
    ]

    examResult = [
            {"Name" : "Alice", "Mark": "A"},
            {"Name" : "Bob", "Mark": "A"},
            {"Name" : "Charlie", "Mark": "B"},
            {"Name" : "Diana", "Mark": "A"},
            {"Name" : "Kevin", "Mark": "A"},
            {"Name" : "Johnson", "Mark": "B"}
        ]

    return render_template('index.html', student_list=students, examinationResult=examResult)

if __name__ == '__main__':
    app.run(debug=True)                                                             