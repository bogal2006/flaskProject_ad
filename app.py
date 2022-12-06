from flask import Flask, redirect, url_for, request, session
from markupsafe import escape
import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(minutes=5)

app.secret_key = 'asdf'


@app.post('/auth')
def auth_method():
    session['auth'] = request.form.to_dict()['user']
    return redirect(url_for('main_2'))


@app.route('/')
def main_2():
    if 'auth' not in session:
        return '<form action="/auth" method ="post"><input name="user"><input type="submit"></form>'
    else:
        u = session['auth']
        return f'Hello {u}'


"""
@app.get('/')
def counter():
    if 'k' not in session:
        session['k'] = 0
    else:
        session['k'] = session['k'] + 1
    k = session['k']
    return f'зашли {k} раз'



@app.route('/', methods=['GET', 'POST'])
def first_web():
    if request.method == "POST":
        return '<h1>Hello World! (POST) </h1>'
    else:
        return '<h1> Hello World! (GET) </h1> <form method="POST"><input type="submit"</form>'



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/user/<int:user_id>')
def test(user_id):
    return f'user n{user_id}'


@app.route('/redir')
def redir():
    return redirect(url_for('hello_world'))



@app.route('/<name_1>')
def hello(name_1):
    return f'hello{escape(name_1)}'
"""

if __name__ == '__main__':
    app.run()
