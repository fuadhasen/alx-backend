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
    guser_id = request.args.get('login_as')
    if guser_id is not None and guser_id.isdigit():
        guser_id = int(guser_id)
        _dict = users.get(guser_id)
        if _dict['locale'] in app.config['LANGUAGES']:
            return _dict
        _dict['locale'] = app.config['BABEL_DEFAULT_LOCALE']
        return _dict
    return None


@app.before_request
def before_request():
    """befor request befor all function"""
    g.user = get_user()
    


@babel.localeselector
def get_local():
    """localisation function"""
    return request.args.get('locale', 'en')


@app.route('/')
def index():
    """index function"""

    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run()
