import os
from flask import Flask, session, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    years_active = db.Column(db.Text)
    courses = db.relationship('Movie', backref='director', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    genre = db.Column(db.String(64))
    year = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))


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


@app.route('/directors')
def show_all_directors():
    directors = Director.query.all()
    return render_template('director-all.html', directors=directors)

## add route for /directors/add Here

## add route for /directors/edit Here

## add route for /directors/delete Here


@app.route('/movie-directory')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)

## add route for /movies/add Here

## add route for /movies/edit Here

## add route for /movies/delete here


@app.route('/movies') ## populate the arrays with whatever real data is put in the manage.py database
def get_all_movies():
    movies = [
        ['Movie1', 'Genre1','Description1'],
        ['Movie2', 'Genre2','Description2'],
        ['Movie3', 'Genre3','Description3']
    ]
    return render_template('movies.html', movies=movies)


if __name__ == '__main__':
    app.run()
