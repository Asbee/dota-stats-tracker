## POPULATES DATABASE WITH DOTA 2 HEROES ID AND NAME ##

import requests
from db import get_db_connection

heroes_response = requests.get("https://api.opendota.com/api/heroes")
heroes = heroes_response.json()

conn = get_db_connection()
cur = conn.cursor()
try:
    for i in heroes:

        hero_id = i["id"]
        hero_name = i["localized_name"]

        cur.execute(
            """
        INSERT INTO heroes (id, name) 
        VALUES (%s, %s) 
        ON CONFLICT (id) DO NOTHING
        """,
            (hero_id, hero_name),
        )

    conn.commit()
finally:
    cur.close()
    conn.close()
