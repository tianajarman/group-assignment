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
    movies = db.relationship('Movie', backref='director', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    genre = db.Column(db.String(64))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
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


@app.route('/directors/add', methods=['GET', 'POST'])
def add_directors():
    if request.method == 'GET':
        return render_template('directors-add.html')
    if request.method == 'POST':
        name = request.form['name']
        years_active = request.form['years_active']

        director = Director(name=name, years_active=years_active)
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/directors/edit/<int:id>', methods=['GET', 'POST'])
def edit_directors(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('directors-edit.html', director=director)
    if request.method == 'POST':
        director.name = request.form['name']
        director.years_active = request.form['years_active']
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/directors/delete/<int:id>', methods=['GET', 'POST'])
def delete_director(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('directors-delete.html', director=director)
    if request.method == 'POST':
        db.session.delete(director)
        db.session.commit()
        return redirect(url_for('show_all_directors'))


@app.route('/movie-directory')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)


@app.route('/movie-directory/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        return render_template('movies-add.html')
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        year = request.form['year']
        description = request.form['description']
        director_name = request.form['director_name']

        director = Director.query.filter_by(name=director_name).first()

        movie = Movie(title=title, genre=genre, year=year, description=description)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie-directory/edit/<int:id>', methods=['GET', 'POST'])
def edit_movies(id):
    movie = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('movies-edit.html', movie=movie)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.genre = request.form['genre']
        movie.year = request.form['year']
        movie.description = request.form['description']
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie-directory/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('movies-delete.html', movie=movie)
    if request.method == 'POST':
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movies')
def get_all_movies():
    movies = [
        ['1', 'Hocus Pocus', 'Comedy', 'After three centuries, three witch sisters are resurrected in Salem, Massachusetts on Halloween night, and it is up to two teenagers, a young girl, and an immortal cat to put an end to their reign of terror once and for all.'],
        ['2', 'Horrible Bosses', 'Comedy', 'Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.'],
        ['3', 'Swimfan', 'Thriller', "A high school senior with a promising swimming career has a one-night stand with consequences."]
    ]
    return render_template('movies.html', movies=movies)


if __name__ == '__main__':
    app.run()
