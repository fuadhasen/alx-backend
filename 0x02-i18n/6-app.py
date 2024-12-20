#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template, request, g
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
        return users.get(guser_id)
    return None


@app.before_request
def before_request():
    """befor request befor all function"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """localisation function"""
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang

    if g.user and g.user.get('locale') is not None:
        user_local = g.user.get('locale')
        if user_local in app.config['LANGUAGES']:
            return g.user.get('locale')

    best = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best:
        return best
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """index function"""

    return render_template('5-index.html', user=g.user)


if __name__ == "__main__":
    app.run()
