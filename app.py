from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    conn.close()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_sqlite_db()
    # होस्ट 0.0.0.0 ठेवल्यामुळे हा ॲप डकरमध्ये अगदी सहज चालेल
    app.run(host='0.0.0.0', port=5000, debug=True)