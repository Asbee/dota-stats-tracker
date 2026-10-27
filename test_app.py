from decimal import Decimal
import app as app_module


def test_home_page_shows_stats(monkeypatch):
    monkeypatch.setattr(app_module, "get_winrate", lambda: Decimal("75"))
    monkeypatch.setattr(app_module, "get_most_played_hero", lambda: ("TestHero", 3))
    monkeypatch.setattr(app_module, "get_avg_kills", lambda: Decimal("4.75"))

    client = app_module.app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "75.0" in html
    assert "TestHero" in html
    assert "4.75" in html
