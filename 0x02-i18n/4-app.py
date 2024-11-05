#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_local():
    """localisation function"""
    lang = request.args.get('locale', 'en')
    if lang and lang in app.config['LANGUAGES']:
        return lang


@app.route('/')
def index():
    """index function"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
