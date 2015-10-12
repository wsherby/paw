from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies_db_setup import Shelter, Puppy, Owner, Base

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/paw/')
@app.route('/paw/home/')
def pawHome():
	shelters = session.query(Shelter).all()
	return render_template('pawhome.html', shelters=shelters)

@app.route('/paw/shelter/<int:shelter_id>/')
def shelterHome(shelter_id):
	shelter = session.query(Shelter).filter_by(id=shelter_id).one()
	puppies = session.query(Puppy).filter_by(shelter_id=shelter_id).all()
	return render_template('shelterhome.html', shelter=shelter, puppies=puppies)

@app.route('/paw/shelter/<int:shelter_id>/puppyprofile/<int:puppy_id>/')
def puppyProfile(shelter_id, puppy_id):
	shelter = session.query(Shelter).filter_by(id=shelter_id).one()
	puppy = session.query(Puppy).filter_by(id=puppy_id).one()
	return render_template('puppyprofile.html', shelter=shelter, puppy=puppy)

if __name__ == '__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run(host='0.0.0.0', port=8888)