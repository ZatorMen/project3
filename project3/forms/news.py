from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    fio = StringField('ФИО', validators=[DataRequired()])
    phone = StringField('Номер тедефона')
    about = TextAreaField("Симптомы")
    photo = FileField('Фото полиса')
    sex = SelectField('Укажите пол', choices=("мужской", "женский"))
    is_private = BooleanField()
    submit = SubmitField('Применить')
