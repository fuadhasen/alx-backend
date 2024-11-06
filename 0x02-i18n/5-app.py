#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template, request, g
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)


class Config:
    """class for app configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """method to get users"""
    user_id = request.args.get('login_as')
    if user_id not in users or not user_id:
        return None
    return users[user_id]


@app.before_request
def before_request():
    """method excuted befor all function"""
    user_dict = get_user()
    g.user = user_dict

@babel.localeselector
def get_locale():
    """localisation function"""
    lang = request.args.get('locale', 'en')
    if lang and lang in app.config['LANGUAGES']:
        return lang


@app.route('/')
def index():
    """index function"""
    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run()
