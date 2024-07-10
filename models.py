from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Note {self.title}>'
