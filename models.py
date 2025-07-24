#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model."""
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import text

db = SQLAlchemy()


class Guests(db.Model):
    """Reg of unique customers."""

    __tablename__ = 'guests'

    ids = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(db.String(20), unique=False, nullable=True)
    user_agent = db.Column(db.Text, unique=False, nullable=True)
    visittime = db.Column(db.DateTime, server_default=text("DATETIME('now', '+3 hours')"))  # SQL method (Europe/Moscow)
    #  visittime = db.Column(DateTime, server_default=func.now()) Native method
