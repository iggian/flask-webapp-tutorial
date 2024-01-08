import json
from flask import Blueprint, flash, render_template, request
from flask_login import current_user, login_required

from .models import Note, db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get("note", "")
        if len(note) < 1:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(data=note, user=str(current_user.id))
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")


    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = json.loads(request.data)
    note_id = data["noteId"] 
    note = Note.query.get(str(note_id))
    if note and note.user == current_user.id:
        db.session.delete(note)
        db.session.commit()

    return jsonfy({})
