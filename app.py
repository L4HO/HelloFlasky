from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"

bootstrap = Bootstrap5(app)


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    name = "Stranger"

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""

    return render_template("hello.html", form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)