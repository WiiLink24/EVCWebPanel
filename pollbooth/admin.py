from flask import url_for, render_template
from flask_oidc import OpenIDConnect
from werkzeug.utils import redirect

from app import app

import config

oidc = OpenIDConnect(app)

@app.context_processor
def inject_oidc():
    return dict(oidc=oidc)

@app.route("/thepollbooth")
@app.route("/thepollbooth/")
def root():
    return redirect(url_for("login"))


@app.route("/thepollbooth/login")
def login():
    if oidc.user_loggedin:
        return redirect(url_for("admin"))

    return render_template("login.html")

@app.route("/thepollbooth/logout")
@oidc.require_login
def logout():
    oidc.logout()
    response = redirect(config.oidc_logout_url)
    response.set_cookie("session", expires=0)
    return response


@app.route("/thepollbooth/admin")
@oidc.require_login
def admin():
    return render_template("pollbooth.html")
