# Created by Davide Sordi in 14/04/2018 at 12.24

from flask import Flask, render_template, url_for, request, redirect, session
import userDB

# First of all
app = Flask(__name__)  # creation of app object
app.secret_key = "tryToGuessMySecretKeyDude123"  # define a secret key for cookies


# this will be a web page
@app.route('/')  # web addr
def starting():
    # return render_template("index.html")
    return redirect(url_for('index'))


@app.route('/index')
def index():
    # posso controllare che non sia vuoto lo user della sessione oppure uso get e il valore di default
    username = session.get("user", "")
    if username != "":
        alarms = userDB.get_alarms(session["id"])
        # print(alarms)
    else:
        alarms = None
    return render_template("index.html", name=username, alarms=alarms)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/welcome", methods=['POST'])
def welcome():
    print(request)
    username = request.form['username']  # this was intended before the cookies implementation
    userdata = userDB.check_user(username)
    if userdata is None:
        return render_template("loginerror.html")  # pagina di errore in caso di username non nel DB
    else:
        session["user"] = userdata[1]  # save the cookies
        session["fullname"] = userdata[3]  # save the cookies
        session["id"] = userdata[0]  # save the cookies
        # print(session["id"])
        # return render_template("welcome.html", name=username)
        return redirect(url_for("index"))


@app.route("/logout")
def logout():
    del (session["user"])
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
