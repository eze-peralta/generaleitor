class Player:
    """
    Represents a player in a generala game

    """
    def __init__(self, name, rolls, complete=False):
        self.name = name
        self.rolls = rolls
        self.scores = {
            k: -1 for k, v in rolls.items()
        }
        self.total = 0
        self.completed = {
            k: False for k in rolls.keys()
        }
        self.complete = complete

    def add_score(self, roll, value):
        if roll not in self.rolls.keys():
            raise ValueError(f"Error: Ingresar un valor válido para tirada {list(self.rolls.keys())}")
        if value not in self.rolls[roll]:
            raise ValueError(f"Error: Ingresar un valor válido para {roll} {self.rolls[roll]}")

        for k in self.rolls.keys():
            if roll == k:
                self.scores[roll] = value
                self.completed[roll] = True

        self.update_total()

    def get_remaining_rolls(self):
        return [
            k for k, v in self.completed.items() if not v
    ]

    def update_total(self):
        total = 0
        for key in self.rolls.keys():
            if self.scores[key] != -1:
                total += self.scores[key]
        self.total = total
        self.complete = all(self.completed.values())
