#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from flask import Flask, render_template, request

from models import Guests, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db.init_app(app)


@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    with app.app_context():
        db.create_all()
        new_entry = Guests(
            ip=request.headers.get('X-Real-IP'),
            user_agent=request.user_agent.string
        )
        db.session.add(new_entry)
        db.session.commit()
    return render_template('index.html')


@app.route('/print')
def print_sqlite():
    """Print visitors, count."""
    res = Guests.query.all()
    lst: list = [[person.ip, person.user_agent, person.visittime] for person in res]
    return render_template('print.html', vst=lst)


if __name__ == '__main__':
    app.run(debug=True)
