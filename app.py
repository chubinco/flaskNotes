from flask import Flask, render_template, redirect, url_for, flash, request
from forms import NoteForm
from models import Note, db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    notes = db.session.execute(db.select(Note).order_by(Note.id)).scalars()
    # notes = Note.query.all()
    return render_template('index.html', notes=notes)


@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    form = NoteForm()
    if request.method == 'POST':
        file = form.file.data
        filename = None
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        note = Note(title=form.title.data,
                    date=form.date.data,
                    category=form.category.data,
                    content=form.content.data,
                    file=filename)
        db.session.add(note)
        db.session.commit()
        flash('Новая заметка успешно добавлена!')
        return redirect(url_for('message'))
    return render_template('add_note.html', mode=form)


@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def note_detail(note_id):
    note = db.get_or_404(Note, note_id)
    return render_template('note.html', memo=note)


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    form = NoteForm(obj=note)
    if form.validate_on_submit():
        file = form.file.data
        filename = note.file
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        note.title = form.title.data
        note.date = form.date.data
        note.category = form.category.data
        note.content = form.content.data
        note.file = filename
        db.session.commit()
        flash('Заметка успешно обновлена')
        return redirect(url_for('message'))
    return render_template('edit_note.html', form=form, note=note)


@app.route('/message')
def message():
    return render_template('message.html')


if __name__ == '__main__':
    app.run(debug=True)
