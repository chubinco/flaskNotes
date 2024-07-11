from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, \
    DateTimeField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired
from datetime import datetime


class NoteForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('Заголовок', validators=[DataRequired()])
    date = DateTimeField('Дата', default=datetime.today())
    category = SelectField('Категория',
                           choices=[('работа', 'Работа'),
                                    ('личное', 'Личное'),
                                    ('путешествие', 'Путешествие'),
                                    ('друзья', 'Друзья'),
                                    ('семья', 'Семья'),
                                    ('волонтерство', 'Волонтерство')],
                           validators=[DataRequired()])
    content = TextAreaField('Заметка', validators=[DataRequired()])
    file = FileField('Файл')
