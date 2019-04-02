from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from models import Category


class BookForm(FlaskForm):
    id = HiddenField('')
    title = StringField('Title', [DataRequired()])
    author = StringField('Author', [DataRequired()])
    year = IntegerField('Year', [DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])
    category = StringField('Category', [DataRequired()])
    save = SubmitField('Save')


class CategoryForm(FlaskForm):
    id = HiddenField('')
    name = StringField('Name', [DataRequired()])
    save = SubmitField('Save')
