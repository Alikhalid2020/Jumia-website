from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,FileField,IntegerField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit') 


class ProductForm(FlaskForm):
    name= StringField('name', validators=[Required()])
    category = SelectField('Category', choices=[('Watch','Watch'),('Television','Television'),('Phones','Phones'),('Bicycles','Bicycles')],validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    price = IntegerField('Price', validators=[Required()])
    image =  FileField('image'),
    submit = SubmitField('Submit')
