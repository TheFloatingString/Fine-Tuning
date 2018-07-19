from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/enter_study')
def enter_study():
    return render_template("enter_study.html")


@app.route('/test_schedule')
def test_schedule():
    return render_template("schedule_test.html")


@app.route('/test_result')
def test_result():
    return render_template("upload_test.html")


if __name__ == '__main__':
    app.run(debug=True)
