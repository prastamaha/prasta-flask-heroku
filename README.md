# Flask App deploy on Heroku
 
 this is just simple example to create a flask app deployed on heroku

# Folder
    templates   ->  locate all html file at here
    static      ->  in this folder you can make sub folder to define css file or image

# File
    requirements.txt    -> this file contains all dependencies needs for run your program (heroku will install it), check this on your virtual env using 'pip3 freeze'
    Procfile            -> tell heroku to use gunicorn for web server, then the main script is website1 with app for Flask object
    runtime.txt         -> this file contains the python runtime version which will heroku use
