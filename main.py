#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Business card website for study and practice."""
from datetime import datetime
from tools.table import Tables
import pytz
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    """Home page."""
    db = Tables()
    ip_visitor = request.remote_addr
    tmstr = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d(%H:%M:%S)') 
    db.add_info(ip_visitor, tmstr)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
