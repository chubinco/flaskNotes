from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField, \
    DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired


class NoteForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('Заголовок', validators=[DataRequired()])
    date = DateField('Дата', format='%d-%m-%Y', validators=[DataRequired()])
    category = SelectField('Категория',
                           choices=[('работа', 'Работа'),
                                    ('личное', 'Личное'),
                                    ('путешествие', 'Путешествие'),
                                    ('друзья', 'Друзья')],
                           validators=[DataRequired()])
    content = TextAreaField('Заметка', validators=[DataRequired()])
    file = FileField('Файл', validators=[
        FileAllowed(['jpg', 'png', 'pdf', 'docx'],
                    'Только документы и фотографии!!!')])
