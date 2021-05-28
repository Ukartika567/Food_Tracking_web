from sqlalchemy.orm import backref
from .extensions import db

log_food = db.Table('log_food',  
    db.Column('log_id', db.Integer, db.ForeignKey('log.log_id')),
    db.Column('food_id', db.Integer, db.ForeignKey('food.food_id'))
)

class Food(db.Model):
 
    food_id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True, nullable=False)
    proteins=db.Column(db.Integer, nullable=False)
    carbs=db.Column(db.Integer, nullable=False)
    fats=db.Column(db.Integer, nullable=False)

    @property
    def calories(self):
        return self.proteins * 4 + self.carbs * 4 + self.fats * 9

class Log(db.Model):
    log_id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date, nullable=True)
    foods=db.relationship('Food', secondary=log_food, backref=db.backref('logs', lazy='dynamic'))