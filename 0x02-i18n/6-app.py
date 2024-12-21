#!/usr/bin/env python3
"""
Use user preferences for locale
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Babel settings
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve a user dictionary based on the 'login_as' parameter.
    """
    user_id = request.args.get("login_as")
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Execute before all requests to set the current user in Flask's global context.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages, prioritizing user preferences.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    Render the index page with user login information and locale preferences.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
