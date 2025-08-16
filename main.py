#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from flask import Flask, render_template, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap


from models import Guests, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uououo'  # Установите уникальный секретный ключ для админки
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db.init_app(app)

admin = Admin(app, name='Посетители')
admin.add_view(ModelView(Guests, db.session))

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


if __name__ == '__main__':
    app.run(debug=True)
