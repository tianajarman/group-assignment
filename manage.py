from flask_script import Manager
from movie import app, db, Director, Movie


manager = Manager(app)


@manager.command ## populate database with real data
def deploy():
    db.drop_all()
    db.create_all()
    director1 = Director(name='Kenny Ortega', years_active='1980-Present')
    director2 = Director(name='Seth Gordon', years_active='2005-Present')
    director3 = Director(name='John Polson', years_active='1999-2011')
    director4 = Director(name="King Vidor", years_active="1913-1980")
    movie1 = Movie(title='Hocus Pocus', genre='Comedy', year='1993', description="After three centuries, three witch sisters are resurrected in Salem, Massachusetts on Halloween night, and it is up to two teenagers, a young girl, and an immortal cat to put an end to their reign of terror once and for all.", director=director1)
    movie2 = Movie(title='Horrible Bosses', genre='Comedy', year='2011', description="Three friends conspire to murder their awful bosses when they realize they are standing in the way of their happiness.", director=director2)
    movie3 = Movie(title='Swimfan', genre='Thriller', year='2002', description="A high school senior with a promising swimming career has a one-night stand with consequences.", director=director3)
    movie4 = Movie(title="The Wizard of Oz", genre="Science Fiction", year="1939", description="An innocent farm girl whisked out of her mundane earthbound existence into a land of pure imagination", director= director4)
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(director4)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.add(movie4)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
