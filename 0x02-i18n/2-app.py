#!/usr/bin/env python3
"""
This module configures a Flask application with language localization support 
using Flask-Babel. It includes the `get_locale` function to dynamically 
select the user's preferred language and an endpoint for the home page.
"""

from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask app.

    Attributes:
        LANGUAGES (list): Supported languages for localization.
        BABEL_DEFAULT_LOCALE (str): Default locale to be used if none is specified.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for date and time formatting.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """localisation function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """index function"""
    title = "Welcome to Holberton"
    head = "Hello world"
    return render_template('2-index.html', title=title,
                           head=head)


if __name__ == "__main__":
    app.run()
