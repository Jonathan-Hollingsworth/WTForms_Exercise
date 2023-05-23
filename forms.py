from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, URLField, TextAreaField
from wtforms.validators import Optional, InputRequired, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """Form template for adding a pet"""

    name = StringField("Name", validators=[InputRequired(message="Please include a name")])
    
    species = StringField("Species", validators=[InputRequired(message="Please include a species"), AnyOf(['cat', 'dog', 'porcupine'], message="only cats, dogs, and porcupines are allowed")])

    photo = URLField("Photo URL", validators=[Optional()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(0, 30, message="The pet's age must be between 0 and 30")])

    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form template for editing a pet"""

    photo = URLField("Photo URL", validators=[Optional()])

    notes = TextAreaField("Notes", validators=[Optional()])

    available = BooleanField("Available?", validators=[Optional()])