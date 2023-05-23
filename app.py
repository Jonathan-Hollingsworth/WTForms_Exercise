from flask import Flask, redirect, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'Adoptable'
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def show_homepage():
    """Displays the homepage and all pets"""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def process_pet_form():
    """Presents/Handles the AddPetForm"""

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    
    else:
        return render_template('add.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def display_pet_info(pet_id):
    """Displays additional information for a pet and displays/handles the EditPetForm"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/{pet.id}')
    
    else:
        return render_template('pet.html', pet=pet, form=form)