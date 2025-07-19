#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from datetime import datetime

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

import pytz

from tools.table import Tables


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visitors.db'


@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    db = Tables()  # FIX with alchimy!!!
    ip_visitor = request.headers.get('X-Real-IP')
    user_agent = request.user_agent.string
    tmstr = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d(%H:%M:%S)')
    db.add_info(ip_visitor, tmstr, user_agent)
    return render_template('index.html')


@app.route('/print_sqlite3')
def print_sqlite():
    """Print visitors, count."""
    return 'sqlite3'


if __name__ == '__main__':
    app.run(debug=True)
