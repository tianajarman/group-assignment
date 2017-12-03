from flask_script import Manager
from movie import app, db, Director, Movie


manager = Manager(app)


@manager.command ## populate database with real data
def deploy():
    db.drop_all()
    db.create_all()
    director1 = Director(name='test', years_active='1940-present')
    director2 = Director(name='test2', years_active='1994-2017')
    director3 = Director(name='test3', years_active='1994-present')
    movie1 = Movie(title='movie1', genre='genre', year='2010', director=director1)
    movie2 = Movie(title='movie2', genre='genre', year='1999', director=director2)
    movie3 = Movie(title='movie3', genre='genre', year='1940', director=director3)
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
