import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/members')
def get_all_members():
    members = [
        'Tiana Jarman',
        'Riley Spehler',
        'Danielle Dominguez'
    ]
    return render_template('members.html', members=members)


if __name__ == '__main__':
    app.run()
