from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func
import uuid


class User(db.Model, UserMixin):
#    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Note(db.Model):
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    data = db.Column(db.String(1024))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.Column(db.Text, db.ForeignKey(User.id))

