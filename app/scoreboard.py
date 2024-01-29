from abc import ABC, abstractmethod

from texttable import Texttable


class AbstractScoreboard(ABC):
    @abstractmethod
    def show_score(self):
        pass

    @abstractmethod
    def add_player(self, player):
        pass

    @abstractmethod
    def get_player(self, name):
        pass

    @abstractmethod
    def get_winner(self):
        pass


class BaseScoreboard(AbstractScoreboard):
    def __init__(self, rolls, name='scoreboard'):
        self.name: str = name
        self.players = {}
        self.rolls = rolls

    def add_player(self, player):
        self.players[player.name] = player

    def show_score(self):
        raise NotImplementedError("show_score method not implemented")

    def get_player(self, name):
        return self.players[name]

    def get_winner(self):
        raise NotImplementedError("get_winner method not implemented")


class GeneralaScoreboard(BaseScoreboard):

    def show_score(self):
        t = Texttable()
        player_names = [p for p in self.players.keys()]
        row_header = ['Jugador'] + player_names
        t.add_rows([row_header])
        for k, v in self.rolls.items():
            row = [k]
            for n, p in self.players.items():
                value = p.scores[k]
                if value == -1:
                    value = '-'
                if value == 0:
                    value = 'X'
                row.append(value)

            t.add_rows([row_header, row])

        total_row = ['total']
        for n, p in self.players.items():
            v = p.total
            total_row.append(v)
        t.add_rows([row_header, total_row])
        print(t.draw())
        print(f"""Tiradas restantes: """)
        for n, p in self.players.items():
            print(f"""{n}: {p.get_remaining_rolls()}""")

    def get_winner(self):
        totals = [
            {
               n: p.total
            } for n, p in self.players.items()
        ]
        # create sorted list of winners
        winners = sorted(totals, key=lambda x: list(x.values())[0], reverse=True)

        # get the first winner
        winner = winners[0]
        winner_name = list(winner.keys())[0]
        winner_total = list(winner.values())[0]
        print(f"\nEl ganador es {winner_name} con {winner_total} puntos\n")

        # print score ranks sorted by total
        for i, w in enumerate(winners):
            name = list(w.keys())[0]
            total = list(w.values())[0]
            print(f"{i + 1} - {name}: {total} puntos")

        return self.get_player(winner_name)


class ChinChonScoreboard(BaseScoreboard):
    def get_winner(self):
        pass

    def show_score(self):
        pass
