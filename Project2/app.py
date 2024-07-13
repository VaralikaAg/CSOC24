from flask import Flask, render_template, request, g, make_response
import sqlite3
import base64

app = Flask(__name__)

DATABASE = 'Task1/task1.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, one=False):
    cur = get_db().execute(query)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

######################################################################################################

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('taskCookie', "0")
    return resp

######################################################################################################

@app.route('/task1', methods=['GET','POST'])
def task1():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # query = f"SELECT * FROM users WHERE username=? AND password=?"
        # user = query_db(query, (username, password), one=True)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        user = query_db(query, one=True)
        if user:
            return render_template('/Task1/correct.html')
        else:
            return render_template('/Task1/incorrect.html')
    return render_template('/Task1/task1.html')

######################################################################################################

@app.route('/task2', methods=['GET', 'POST'])
def task2():
    resp = make_response(render_template('/Task2/task2.html'))
    resp.set_cookie('taskCookie', "0")
    data = request.cookies.get("taskCookie")      
    if data == '1':
        return render_template('/Task2/cookie.html')
    return render_template('/Task2/task2.html')

######################################################################################################

@app.route('/task3')
def task3():
    return render_template('/Task3/task3.html')

@app.route('/task3/secret')
def secret():
    return render_template('/Task3/secret.html')

@app.route('/task3/secret/hidden')
def hidden():
    return render_template('/Task3/hidden.html')

######################################################################################################

@app.route('/task4')
def task4():
    return render_template('/Task4/task4.html')

######################################################################################################

@app.route('/task5')
def task5():
    msg = "Task 5 Completed!!"
    enc_msg = base64.b64encode(msg.encode())
    resp = make_response(render_template('/Task5/task5.html'))
    resp.headers['web'] = enc_msg
    return resp

######################################################################################################

if __name__ == '__main__':
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        user = query_db("SELECT * FROM users WHERE username='admin'", one=True)
        if not user:
            db.execute('''
                INSERT INTO users (username, password) VALUES ('admin', 'password123');
            ''')
            db.execute('''
                INSERT INTO users (username, password) VALUES ('harry', 'pass');
            ''')
            db.execute('''
                INSERT INTO users (username, password) VALUES ('john', 'xyz');
            ''')
        db.commit()
        db.close()
    
    app.run(debug=True)
