from flask import Flask
from logging import debug
from .main.routes import main
from .extensions import db
from .models import Food


def create_app():
    app=Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/foodtracker'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


    db.init_app(app)

    app.register_blueprint(main)

    return app    

 