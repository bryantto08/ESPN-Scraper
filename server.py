from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    team_leaders = []
    if request.method == "POST":
        team = request.form["team"]
        team_leaders = main.team_leader(team)
    return render_template("index.html", team_leaders=team_leaders)


if __name__ == "__main__":
    app.run()
