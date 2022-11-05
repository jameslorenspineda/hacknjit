from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)