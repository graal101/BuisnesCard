#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from datetime import datetime

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning

db = SQLAlchemy(app)


class Guests(db.Model):
    """Reg of unique customers."""

    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    visittime = db.Column(db.String(25), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)


@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    with app.app_context():
        db.create_all()
        new_entry = Guests(
            ip=request.headers.get('X-Real-IP'),
            visittime=datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d(%H:%M:%S)'),
            user_agent=request.user_agent.string
        )
        db.session.add(new_entry)
        db.session.commit()
    return render_template('index.html')


@app.route('/print')
def print_sqlite():
    """Print visitors, count."""
    res = Guests.query.all()
    lst = [[person.ip, person.visittime, person.user_agent] for person in res]
    return render_template('print.html', vst=lst)


if __name__ == '__main__':
    app.run(debug=True)
