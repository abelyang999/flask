from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addemp', methods = ['POST', 'GET'])
def addemp():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("emp has been added")
        else:
            flash("emp can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updateemp', methods = ['POST'])
def updateemp():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('emp has been updated')

        else:
            flash('emp can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deleteemp', methods = ['POST'])
def deleteemp():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('emp has been deleted')

        else:
            flash('A emp can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
