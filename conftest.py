import pytest
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


@pytest.fixture
def test_db():
    conn = psycopg2.connect(
        dbname="test_database_dota", user=db_user, password=db_password
    )
    cur = conn.cursor()

    # clean database for each test
    cur.execute("TRUNCATE player_matches, players, heroes RESTART IDENTITY CASCADE;")

    # insert known, fixed test data
    cur.execute(
        "INSERT INTO players (steam_id, player_name) VALUES (111, 'TestPlayer');"
    )
    cur.execute(
        "INSERT INTO heroes (id, name) VALUES (1, 'TestHero'), (2, 'OtherHero');"
    )
    cur.execute("""
        INSERT INTO player_matches (player_id, match_id, hero_id, kills, deaths, assists, duration, win) VALUES 
        (1, 1001, 1, 5, 2, 3, 1500, TRUE), 
        (1, 1002, 1, 1, 0, 1, 1200, FALSE), 
        (1, 1003, 1, 10, 0, 5, 1800, TRUE), 
        (1, 1004, 2, 3, 6, 2, 1600, TRUE);
    """)
    conn.commit()

    yield conn

    cur.close()
    conn.close()
