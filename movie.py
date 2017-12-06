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

@app.route('/directors/add')
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
def edit_director(id):
    director = Director.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('directors-edit.html', director=director)
    if request.method == 'POST':
        director.name = request.form['name']
        director.years_active = request.form['years_active']
    db.session.commit
    return redirect(url_for('show_all_directors'))
## add route for /directors/delete Here


@app.route('/movie-directory')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)

@app.route('/movies/add')
def add_movies():
    if request.method == 'GET':
        return render_template('movies-add.html')
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        year = request.form['year']
        director_name = request.form['director_name']

        director = Director.query.filter_by(name=director_name).first()
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


## add route for /movies/delete here


@app.route('/movies')
def get_all_movies():
    movies = [
        ['HocusPocus', 'Comedy', "After moving to Salem, Mass., teenager Max Dennison (Omri Katz) explores an abandoned house with his sister Dani (Thora Birch) and their new friend, Allison (Vinessa Shaw). After dismissing a story Allison tells as superstitious, Max accidentally frees a coven of evil witches (Bette Midler, Sarah Jessica Parker, Kathy Najimy) who used to live in the house. Now, with the help of a magical cat, the kids must steal the witches book of spells to stop them from becoming immortal."],
        ['HorribleBossess', 'Comedy', "Nick (Jason Bateman), Dale (Charlie Day) and Kurt (Jason Sudeikis) are workers who would like nothing better than to grind their oppressive employers into the dirt. Quitting their jobs is not an option, so -- fueled by alcohol and dubious advice from a criminal (Jamie Foxx) -- the men devise a complex and seemingly foolproof plan to permanently rid themselves of their terrible bosses. The problem is, any plan is only as clever as the brains behind it."],
        ['Swimfan', 'Thriller', "Ben Cronin (Jesse Bradford) has it all: the admiration of his many friends, a terrific girlfriend, and he's on the fast-track to an athletic scholarship. Ben's rock-solid, promising future and romance are turned upside-down with the arrival of Madison Bell (Erika Christensen). Madison, the new girl in town, quickly sets her sights on the impressionable Ben. While their first few meetings are innocent enough, the obsessive and seductive Madison wants more ... much more."]
    ]
    return render_template('movies.html', movies=movies)


if __name__ == '__main__':
    app.run()
