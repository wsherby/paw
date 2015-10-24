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

@app.route('/paw/admin')
def admin():
	return render_template('admin.html')

@app.route('/paw/admin/shelter')
def shelter_admin():
	shelters = session.query(Shelter).all()
	return render_template('shelter_admin.html', shelters = shelters)

@app.route('/paw/admin/puppies')
def puppies_admin():
	return render_template('shelter_puppies.html')

@app.route('/paw/admin/owners')
def owners_admin():
	return render_template('shelter_owners.html')

@app.route('/paw/admin/shelter/<int:shelter_id>/edit/', methods = ['GET', 'POST'])
def edit_shelter(shelter_id):
	shelter = session.query(Shelter).filter_by(id=shelter_id).one()
	if request.method == 'POST':
		shelter.name = request.form['name']
		shelter.address = request.form['address']
		shelter.city = request.form['city']
		shelter.state = request.form['state']
		shelter.zipcode = request.form['zipcode']
		shelter.email = request.form['email']
		session.add(shelter)
		session.commit()
		flash("shelter %s edited successfully!" % shelter.name)
		return redirect(url_for('shelter_admin'))
	return render_template('edit_shelter.html', shelter = shelter)


if __name__ == '__main__':
	app.secret_key = "super_secret_key"
	app.debug = True
	app.run(host='0.0.0.0', port=8888)