import requests
from db import get_db_connection

account_id = 71920194
recent_matches = f"https://api.opendota.com/api/players/{account_id}/matches?limit=100"
response = requests.get(recent_matches)
result = response.json()


# Handles match data insertion to database
def save_match_data(data):

    conn = get_db_connection()
    cur = conn.cursor()

    # Insert match data to database.
    try:
        for i in data:

            win = compute_win(i["player_slot"], i["radiant_win"])
            match_id = i["match_id"]
            hero_id = i["hero_id"]
            kills = i["kills"]
            deaths = i["deaths"]
            assists = i["assists"]
            duration = i["duration"]

            cur.execute(
                """
                    INSERT INTO player_matches (player_id, match_id, hero_id, kills, deaths, assists, duration, win)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (player_id, match_id) DO NOTHING
                    """,
                (1, match_id, hero_id, kills, deaths, assists, duration, win),
            )

        conn.commit()
    finally:
        cur.close()
        conn.close()


## check if player won his match or lost it
def compute_win(player_slot, radiant_win):
    if player_slot >= 0 and player_slot <= 4 and radiant_win == True:
        win = True
    elif player_slot >= 128 and radiant_win == False:
        win = True
    else:
        win = False

    return win


save_match_data(result)
