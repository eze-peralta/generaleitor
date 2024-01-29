import pytest

from app.main import ROLLS
from app.player import Player
from app.scoreboard import Scoreboard


def test_get_winner():
    s = Scoreboard(rolls=ROLLS)
    player_1 = Player("Juan", rolls=s.rolls, complete=True)
    player_1.add_score('generala', 50)
    s.add_player(player_1)
    player_2 = Player("Pedro", rolls=s.rolls, complete=True)
    player_2.add_score('doble', 100)
    s.add_player(player_2)
    result = s.get_winner()
    assert result.name == 'Pedro'


def test_invalid_score():
    s = Scoreboard(rolls=ROLLS)
    player_1 = Player("Juan", rolls=s.rolls, complete=False)
    player_2 = Player("Pedro", rolls=s.rolls, complete=False)
    with pytest.raises(ValueError):
        player_2.add_score('generala', 200)