from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length

class AddCategory(FlaskForm):
    category_title = StringField('Category Title', validators=[DataRequired(message="Field is empty"), Length(min=1,max=30)])
    submit = SubmitField('Add')

# class UpdateCategory(FlaskForm):
#     category_title = StringField('Category Title', validators=[DataRequired(message="Field is empty"), Length(min=1,max=30)])
#     submit = SubmitField('Update')

class AddTask(FlaskForm):
    description = StringField('Task', validators=[DataRequired(message="Field is empty"), Length(min=1,max=100)])
    date = DateField('Due Date', validators=[DataRequired("Field is empty")])
    category = SelectField('Category', choices=[])
    submit = SubmitField('Add')

class UpdateTask(FlaskForm):
    description = StringField('Task', validators=[DataRequired(message="Field is empty"), Length(min=1,max=100)])
    date = DateField('Due Date', validators=[DataRequired("Field is empty")])
    submit = SubmitField('Update')

# class FilterBy(FlaskForm):
#     category = SelectField('Filter by Category', validators=[DataRequired(message='No Data')], choices=[('All','All')])
#     submit = SubmitField('Filter')
  

