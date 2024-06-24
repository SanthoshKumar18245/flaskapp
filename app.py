from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# MySQL configuration
db = mysql.connector.connect(
    host="192.168.1.158",
    user="santhosh",
    password="Santhosh@123",
    database="user"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO data (user, email) VALUES (%s, %s)", (name, email))
        db.commit()
        cursor.close()
        
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
