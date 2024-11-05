#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """get user function"""
    guser_id = request.args.get('login_as', type=int)
    if guser_id and guser_id in users:
        return guser_id
    return None


@app.before_request
def before_request():
    """befor request befor all function"""
    user_id = get_user()
    if user_id:
        g.user_id = user_id


@babel.localeselector
def get_local():
    """localisation function"""
    lang = request.args.get('locale', 'en')
    if lang:
        return lang

    if g.user_id:
        user_local = users[g.user].get('locale')
        if user_local:
            return user_local
    return request.accept_languages.best_match(app.config['LANGUAGES'])
  
    


@app.route('/')
def index():
    """index function"""
    title = "Welcome to Holberton"
    head = "Hello world"
    return render_template('5-index.html', title=title,
                           head=head, user=g.user_id)


if __name__ == "__main__":
    app.run()

