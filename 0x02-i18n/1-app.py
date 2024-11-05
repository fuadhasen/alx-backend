#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """index function"""
    title = 'Welcome to Holberton'
    head = 'Hello world'
    return render_template('1-index.html', title=title,
                           head=head)


if __name__ == "__main__":
    app.run()
