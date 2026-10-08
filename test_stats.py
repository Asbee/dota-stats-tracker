from stats import get_most_played_hero, get_winrate


def test_get_most_played_hero(test_db):
    result = get_most_played_hero(test_db)
    assert result == ("TestHero", 3)


def test_get_winrate(test_db):
    result = get_winrate(test_db)
    assert result == 75
