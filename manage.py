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
    movie1 = Movie(title='Hocus Pocus', genre='Comedy', year='1993', director=director1, description="After moving to Salem, Mass., teenager Max Dennison (Omri Katz) explores an abandoned house with his sister Dani (Thora Birch) and their new friend, Allison (Vinessa Shaw). After dismissing a story Allison tells as superstitious, Max accidentally frees a coven of evil witches (Bette Midler, Sarah Jessica Parker, Kathy Najimy) who used to live in the house. Now, with the help of a magical cat, the kids must steal the witches' book of spells to stop them from becoming immortal.")
    movie2 = Movie(title='Horrible Bosses', genre='Comedy', year='2011', director=director2, description="Nick (Jason Bateman), Dale (Charlie Day) and Kurt (Jason Sudeikis) are workers who would like nothing better than to grind their oppressive employers into the dirt. Quitting their jobs is not an option, so -- fueled by alcohol and dubious advice from a criminal (Jamie Foxx) -- the men devise a complex and seemingly foolproof plan to permanently rid themselves of their terrible bosses. The problem is, any plan is only as clever as the brains behind it.")
    movie3 = Movie(title='Swimfan', genre='Thriller', year='2002', director=director3, description="Ben Cronin (Jesse Bradford) has it all: the admiration of his many friends, a terrific girlfriend, and he's on the fast-track to an athletic scholarship. Ben's rock-solid, promising future and romance are turned upside-down with the arrival of Madison Bell (Erika Christensen). Madison, the new girl in town, quickly sets her sights on the impressionable Ben. While their first few meetings are innocent enough, the obsessive and seductive Madison wants more ... much more.")
    db.session.add(director1)
    db.session.add(director2)
    db.session.add(director3)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
