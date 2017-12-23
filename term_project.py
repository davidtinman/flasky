import os
from flask import Flask, render_template, session, redirect, url_for
from flask_BOOTSTRAP import Bootstrap
from flask_MOMENT import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from sqlalchemy.sql import func

BASEDIR = os.path.abspath(os.path.dirname(__file__))

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'hard to guess string'
APP.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(BASEDIR, 'data.sqlite')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MANAGER = Manager(APP)

BOOTSTRAP = Bootstrap(APP)
MOMENT = Moment(APP)
DB = SQLAlchemy(APP)


class Food(DB.Model):
    """The main food groups recognized by the USDA"""
    __tablename__ = 'foods'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(64), unique=True)
    macronutrients = DB.relationship('Macronutrient', backref='food', lazy='dynamic')

    def __repr__(self):
        return '<Food %r>' % self.name

class Macronutrient(DB.Model):
    """Macronutrients inclued protein, carbohydrates, and fat."""
    __tablename__ = 'macronutrients'
    id = DB.Column(DB.Integer, primary_key=True)
    major_macronutrient = DB.Column(DB.String(64), unique=True, index=True)
    food_id = DB.Column(DB.Integer, DB.ForeignKey('foods.id'))

    def __repr__(self):
        return '<Macronutrient %r' %self.major_macronutrient

class User(DB.Model):
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FoodForm(FlaskForm):
    name = SelectField(u'Category',
                       choices=[('Fruit', 'Fruit'), ('Vegetables', 'Vegetables'),
                                ('Grains', 'Grains'), ('Protein Foods', 'Protein Foods'),
                                ('Dairy', 'Dairy'), ('Added Sugar', 'Added Sugar')])
    submit = SubmitField('Submit')

class MacronutrientForm(FlaskForm):
    major_macronutrient = SelectField(u'Category',
                                      choices=[('Protein', 'Protein'),
                                               ('Fat', 'Fat'),
                                               ('Carbohydrates', 'Carbohydrates')])
    submit = SubmitField('Submit')

@APP.shell_context_processor
def make_shell_context():
    return dict(DB=DB, User=User, Role=Role)


@APP.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@APP.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@APP.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            DB.session.add(user)
            DB.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@APP.route('/food', methods=['GET', 'POST'])
def food():
    form = FoodForm()
    if form.validate_on_submit():
        food = Food.query.filter_by(name=form.name.data).first()
        if food is None:
            food = Food(name=form.name.data)
            DB.session.add(food)
            DB.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('food'),
                           known=session.get('known', False))

@APP.route('/macro', methods=['GET', 'POST'])
def macro():
    form = MacronutrientForm()
    if form.validate_on_submit():
        macronutrient = Macronutrient.query.filter_by(major_macronutrient=form.name.data).first()
        if macronutrient is None:
            macronutrient = Macronutrient(major_macronutrient=form.name.data)
            DB.session.add(macronutrient)
            DB.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('macronutrient'),
                           known=session.get('known', False))

@APP.route('/food/count')
def show_food():
    food_count = DB.session.query(Food, func.count('food')).all()
    return render_template('show_food.html', food_count=food_count)

if __name__ == '__main__':
    APP.run(debug=True)
