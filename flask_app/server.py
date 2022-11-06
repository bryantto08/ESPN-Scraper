from flask import Flask, render_template, request
import scraper

app = Flask(__name__)


# Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# Team Leaders Page
@app.route("/team_leaders", methods=["GET", "POST"])
def team_leaders():
    info = [[], []]  # stores info and sends it to html
    if request.method == "POST":
        team = request.form["team"]
        info = scraper.team_leader(team)
    return render_template("team_leaders.html", team_leaders=info[0], logo=info[1])


# Players Stats page
@app.route("/player_stats", methods=["GET", "POST"])
def player_stats():
    info = [[], [], []]
    if request.method == "POST":  # User input from page
        name = request.form["name"]
        position = request.form["position"]
        info[0] = name
        info[1], info[2] = scraper.player_stats(name, position)

    return render_template("player_stats.html", name=info[0], stats=info[1], logo=info[2])

#TODO: News, specific player stats


if __name__ == "__main__":
    app.run(debug=True)
