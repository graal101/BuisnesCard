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

class Users(db.Model):
    """Reg of unique customers."""   
    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    visittime = db.Column(db.String(25), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)



@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    ip_visitor = request.headers.get('X-Real-IP')
    user_agent = request.user_agent.string
    tmstr = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d(%H:%M:%S)')
    with app.app_context():
        db.create_all()
        new_entry = Users(ip=ip_visitor, visittime=tmstr, user_agent=user_agent)
        db.session.add(new_entry)
        db.session.commit()
    return render_template('index.html')


@app.route('/print_sqlite3')
def print_sqlite():
    """Print visitors, count."""
    return 'sqlite3'


if __name__ == '__main__':
    app.run(debug=True)
