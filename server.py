from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/team_leaders", methods=["GET", "POST"])
def team_leaders():
    team_leaders = []
    if request.method == "POST":
        team = request.form["team"]
        team_leaders = main.team_leader(team)
    return render_template("team_leaders.html", team_leaders=team_leaders)


@app.route("/player_stats", methods=["GET", "POST"])
def player_stats():
    return

#TODO: News, specific player stats


if __name__ == "__main__":
    app.run()
