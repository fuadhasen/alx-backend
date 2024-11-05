#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """index function"""
    title = 'Welcome to Holberton'
    head = 'Hello world'
    return render_template('0-index.html', title=title,
                           head=head)


if __name__ == "__main__":
    app.run()
