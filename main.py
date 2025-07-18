#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from datetime import datetime

from flask import Flask, render_template, request

import pytz

from tools.table import Tables


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    db = Tables()  # FIX with alchimy!!!
    ip_visitor = request.headers.get('X-Real-IP')
    # ip_visitor = request.remote_addr
    # ip_visitor = request.headers.get('X-Forwarded-For')
    # user_agent = request.user_agent.string
    tmstr = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d(%H:%M:%S)')
    db.add_info(ip_visitor, tmstr)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
