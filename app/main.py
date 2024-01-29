from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from app.player import Player
from app.scoreboard import GeneralaScoreboard, ChinChonScoreboard


from kivy.app import App
from kivy.uix.widget import Widget




ROLLS = {
    'unos': [0, 1, 2, 3, 4, 5],
    # 'score': [i for i in range(101)],
    'dos': [0, 2, 4, 6, 8, 10],
    'tres': [0, 3, 6, 9, 12, 15],
    'cuatros': [0, 4, 8, 12, 16, 20],
    'cincos': [0, 5, 10, 15, 20, 25],
    'seis': [0, 6, 12, 18, 24, 30],
    # 'sietes': [0, 7, 14, 21, 8, 35],
    'escalera': [0, 20, 25],
    'full': [0, 30, 35],
    'poker': [0, 40, 45],
    'generala': [0, 50],
    'doble': [0, 100]
}

games = {
    'generala': GeneralaScoreboard,
    'chinchon': ChinChonScoreboard
}


class Application:
    """
    Application to keep score of a tabletop generala game

    User inputs score for each roll turn
    """
    def __init__(self):
        self.name = "Generaleitor"

    def run(self):
        input_players = True
        scoreboard = GeneralaScoreboard(rolls=ROLLS, name='generaleitor')
        print(f"""
        Bienvenido a {scoreboard.name}
        
        Ingrese el nombre de los jugadores.
        Ingrese q para seguir
        
        """)
        while input_players:
            name = input("Ingresar nombre: ")
            if name == "q":
                input_players = False
            else:
                p = Player(name, rolls=scoreboard.rolls)
                scoreboard.add_player(p)

        print(f"""
        \nJugadores:
        {list(scoreboard.players.keys())}
        """)

        print(f"""
        Ingrese el nombre del jugador que tiró
        e ingrese puntaje para la tirada.
        p ej: "{list(scoreboard.players.keys())[0]} {list(scoreboard.rolls.keys())[0]} {list(scoreboard.rolls.values())[0][1]}"\n
        Ingrese 0 para tachar, p ej,
        "{list(scoreboard.players.keys())[0]} {list(scoreboard.rolls.keys())[0]} 0" para tachar los unos\n\n
        """)

        input_score = True
        while input_score:
            score = input("\nJugador tirada valor: ").split(" ")

            # validate player
            name = score[0]
            if name not in scoreboard.players.keys() or not name:
                print(f"""
                    Error: Ingrese un valor válido en el siguiente formato:\n
                    jugador tirada valor\n
                    p ej: "{list(scoreboard.players.keys())[0]} {list(scoreboard.rolls.keys())[0]} {list(scoreboard.rolls.values())[0][1]}"\n    
                    jugadores: {list(scoreboard.players.keys())}                
                    """)
                continue

            # validate roll
            try:
                p = scoreboard.get_player(name)
                roll = score[1]
                value = int(score[2])
                p.add_score(roll, value)
            except ValueError as e:
                print(e)
                continue
            except IndexError:
                print(
                    f"""
                \nError: Ingrese un valor válido en el siguiente formato: \n
                jugador tirada valor \n
                p ej: "{list(scoreboard.players.keys())[0]} {list(scoreboard.rolls.keys())[0]} {list(scoreboard.rolls.values())[0]}"\n
                """
                )
                continue

            # show scoreboard
            scoreboard.show_score()

            # check if all players are complete
            # if so, end game
            complete_players = all([
                p.complete for p in scoreboard.players.values()
            ])
            if complete_players:
                print("\n\nTodos los jugadores completaron su puntaje\n")
                print("Fin del juego")
                input_score = False

        # determine winner
        scoreboard.get_winner()
        scoreboard.show_score()


class PongGame(GridLayout):
    def __init__(self, **kwargs):
        self.players = [Player('eze', ROLLS), Player('dami', ROLLS)]
        GridLayout.__init__(self, rows=0, cols=0)
        self.cols = len(self.players) + 1
        self.rows = len(ROLLS.keys()) + 2

        # add header row
        for i in range(self.cols):
            if i == 0:
                self.add_widget(Label(text='Jugador'))
            else:
                self.add_widget(Label(text=list(self.players)[i-1].name))

        # add rolls rows
        for j in ROLLS.keys():
            self.add_widget(Label(text=j))
            for i, player in enumerate(self.players):
                self.add_widget(Button(text=str(player.scores[j])))

        # add totals row
        for i in range(self.cols):
            if i == 0:
                self.add_widget(Label(text='Total'))
            else:
                self.add_widget(Label(text=''))


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()




# if __name__ == "__main__":
#
#     app.run()