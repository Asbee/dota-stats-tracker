from flask import Flask
from stats import get_avg_kills, get_most_played_hero, get_winrate

app = Flask(__name__)


@app.route("/")
def show_stats():

    avgkills = get_avg_kills()
    most_played_hero = get_most_played_hero()
    winrate = get_winrate()

    return f"""
    <h1>Your winrate is {winrate:.1f} </h1>
    <p> Your most played hero is {most_played_hero[0]} </p>
    <p> Your average kills in match is {avgkills:.2f} </p>
     """
