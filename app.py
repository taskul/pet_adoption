from flask import Flask, render_template, flash, redirect, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption_forms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    '''Render home page and show all available for adoption pets'''
    pets = Pet.query.filter(Pet.available == True).all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    '''Add new pet'''
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data 
        photo_url = form.photo_url.data 
        age = form.age.data 
        notes = form.notes.data 
        new_friend = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_friend)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_friend.html', form=form)

@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    '''Edit existing pet'''
    pet = Pet.query.get(id)
    form = PetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data 
        pet.species = form.species.data 
        pet.photo_url = form.photo_url.data 
        pet.age = form.age.data 
        pet.notes = form.notes.data 
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)

if __name__ == '__main__':
    app.run(debug=True)