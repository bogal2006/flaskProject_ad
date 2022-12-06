from flask import Flask, redirect, url_for, request, session
import datetime

app = Flask(__name__)
app.permanent_session_lifetime = datetime.timedelta(minutes=5)

app.secret_key = 'asdf'


@app.post('/auth')
def auth_method():
    session['auth'] = request.form.to_dict()['user']
    return redirect(url_for('main_2'))


@app.route('/change')
def change_ad():
    if 'auth' in session:
        return '<h1>Измените объявление </h1> <form action="/auth" method ="post"><input name="user"><input ' \
               'type="submit"></form> '
    else:
        return redirect(url_for('main_2'))


@app.route('/delete')
def delete_ad():
    if 'auth' in session:
        session.pop('auth', None)
        return redirect(url_for('main_2'))
    else:
        redirect(url_for('main_2'))


@app.route('/')
def main_2():
    if 'auth' not in session:
        return '<h1>Введите объявление </h1> <form action="/auth" method ="post"><input name="user"><input ' \
               'type="submit"></form> <h3>Изменить объявление в URL (адресную строку) добавить /change </h3>' \
               '<h3>Удалить объявление в URL(адресную строку) добавить /delete </h3> '
    else:
        u = session['auth']
        return f'<h1>Объявление </h1> {u}<h3>Изменить объявление в URL (адресную строку) добавить /change </h3>' \
               '<h3>Удалить объявление в URL(адресную строку) добавить /delete </h3>'


if __name__ == '__main__':
    app.run()
