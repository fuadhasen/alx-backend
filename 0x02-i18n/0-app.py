#!/usr/bin/env python3
"""scripts for simple flask App"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """index function"""
    title = "Welcome to Holberton"
    head = "Hello world"
    return render_template('0-index.html', title=title,
                           head=head)


if __name__ == "__main__":
    app.run()
