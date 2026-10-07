from db import get_db_connection


def get_most_played_hero():
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT heroes.name, COUNT(*) 
            FROM player_matches 
            JOIN heroes ON player_matches.hero_id = heroes.id 
            GROUP BY heroes.name 
            ORDER BY COUNT(*) DESC LIMIT 1;
            """)
        result = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    return result


def get_winrate():
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
        SELECT COUNT(*) 
        FILTER (WHERE win = TRUE)::numeric / 
        COUNT(*) * 100 
        FROM player_matches;
        """)
        result = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    return result[0]


if __name__ == "__main__":
    print(get_winrate())
