from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="flask_project"
    )

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
