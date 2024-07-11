from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.today())
    category = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    file = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Note {self.title}>'
