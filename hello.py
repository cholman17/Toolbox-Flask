""" CHRISTINA HOLMAN TOOLBOX #4
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/') #INDEX PAGE
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.form['fullname'] == '' or request.form['age'] == '':
        #show errorpage if missed a question
        return render_template('errorpage.html')
    else: #if all info present show results
        name = request.form['fullname']
        age = request.form['age']
        ninja = request.form['ninja'] #Patrick Huston???
        return render_template('profile.html', name=name, age=age, ninja=ninja)

if __name__ == '__main__':
    app.run()
