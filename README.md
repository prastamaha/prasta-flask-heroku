# Flask App deploy on Heroku
 
 this is just simple example to create a flask app deployed on heroku

## Folder
    templates   ->  locate all html file at here
    static      ->  in this folder you can make sub folder to define css file or image

## File
    requirements.txt    -> this file contains all dependencies needs for run your program (heroku will install it), check this on your virtual env using 'pip3 freeze'
    Procfile            -> tell heroku to use gunicorn for web server, then the main script is website1 with app for Flask object
    runtime.txt         -> this file contains the python runtime version which will heroku use

## deploy to heroku

    $ cd /path/your/project
    
    $ heroku login                          # login with your heroku account
    $ heroku create prasta-flask            # create an app with name prasta-flask
    $ heroku apps                           # to list all apps on your account
    $ git init                              # create .git folder
    $ git add .                             # to add all file on your project dir to git
    $ git commit -m 'first commit'          # commit the change
    $ heroku git:remote --app prasta-flask  # tell git to remote prasta-flask for this directory
    $ git push heroku master                # push to the heroku production 

## visit this app

    [https://prasta-flask.herokuapp.com](https://prasta-flask.herokuapp.com)
