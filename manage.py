from flask_script import Manager
from movie import app, db, Director, Movie


manager = Manager(app)


@manager.command ## populate database with real data
def deploy():
    db.drop_all()
    db.create_all()
    director1 = Director(name='Kenny Ortega', years_active='1980-present')
    director2 = Director(name='Seth Gordon', years_active='2005-Present')
    director3 = Director(name='John Polson', years_active='1999-2011')
    movie1 = Movie(title='Hocus Pocus', genre='Comedy', year='1993', director=director1)
    movie2 = Movie(title='Horrible Bosses', genre='Comedy', year='2011', director=director2)
    movie3 = Movie(title='Swimfan', genre='Thriller', year='2002', director=director3)
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
