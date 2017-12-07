# group-assignment

### Group 6 - MISY 350 - Group Project

We're making a database to catalog a list of movies from different genres, along with the director of each movie. We will have a movie table with columns title, genre, and year released. We will also have a director table with columns name and years active. Each movie can only have one director and one director can film many movies, so there is a one-to-many relationship here.

### Database Design
Director ID |  Name | Years Active
------------|---------------|-------------
1 | Kenny Ortega | 1980-Present
2 | Seth Gordon | 2005-Present
3 | John Polson | 1999-2011

Movie ID | Title | Genre | Year | Description| Director
---------|-------|-------|------|------------|---------
1 | Hocus Pocus | Comedy | 1993 | After three centuries, three witch sisters...| Kenny Ortega
2 | Horrible Bosses | Comedy | 2011 | Three friends conspire to murder... | Seth Gordon
3 | Swimfan | Thriller | 2002 | A high school senior with a promising... | John Polson

### Instructions

In order to run our website, you'll need to follow a few simple steps to get it up and running in your web browser of choice.

- **Windows Instructions**

    1. Go to our [repository on Github](http://github.com/tianajarman/group-assignment) and clone the repo so that you can store it locally.

    2. Open Powershell

    3. Type the following command to open the project directory:
            cd group-assignment

    4. Type the following command to create Virtualenv so that we can setup a virtual environment:
            pip install virtualenv

    5. Create the venv folder:
            virtualenv venv

    6. Activate the virtual environment:
            venv/scripts/activate

    7. Install the requirements for the project:
            pip install -r requirements.txt

    8. Initialize the database:
            python manage.py deploy

    9. Run the server:
            python manage.py runserver -d

    10. View the website in your web browser by typing your IP address into the address bar.

- **Mac Instructions**
  1. Go to our [repository on Github](http://github.com/tianajarman/group-assignment) and clone the repo so that you can store it locally.

  2. Open the Command Line

  3. Type the following command to open the project directory:
          cd group-assignment

  4. Type the following command to create Virtualenv so that we can setup a virtual environment:
          sudo pip install virtualenv

  5. Create the venv folder:
          virtualenv venv

  6. Activate the virtual environment:
          venv/bin/activate

  7. Install the requirements for the project:
          pip install -r requirements.txt

  8. Initialize the database:
          python manage.py deploy

  9. Run the server:
          python manage.py runserver -d

  10. View the website in your web browser by typing your IP address into the address bar.
