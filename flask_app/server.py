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


@app.route("/player_stats", methods=["GET", "POST"])
def player_stats():
    info = [[],[]]
    if request.method == "POST":
        name = request.form["name"]
        position = request.form["position"]
        info = scraper.player_stats(name, position)
    return render_template("player_stats.html", stats=info[0], logo=info[1])

#TODO: News, specific player stats


if __name__ == "__main__":
    app.run()
