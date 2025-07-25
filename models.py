#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import  DateTime

db = SQLAlchemy()


class Guests(db.Model):
    """Reg of unique customers."""


    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)
    visittime = db.Column(db.DateTime, server_default=func.now())

