"""
Aidan Butcher
CS 3450 - Algorithms & Data Structures
Python code for a ScoreBoard class that maintains an ordered series of
scores as GameEntry objects.
"""


class GameEntry():
    """Represents one entry of a list of high scores."""

    def __init__(self, name: str, score: int):
        """Initializes the GameEntry with a name and a score."""
        self._name = name
        self._score = score

    def get_name(self) -> str:
        """Returns the name of the object"""
        return self._name

    def get_score(self) -> int:
        """Return the score of the object"""
        return self._score

    def __str__(self) -> str:
        return f"{self._name}, {self._score}"


o_game = GameEntry("James", 90)
o_game2 = GameEntry("Bob", 60)
o_game3 = GameEntry("Charlie", 95)
o_game4 = GameEntry("Patrik", 92)
o_game5 = GameEntry("Carl", 97)
o_game6 = GameEntry("Bobby", 100)
o_game7 = GameEntry("Charles", 50)
o_game8 = GameEntry("Banana", 92)
o_game9 = GameEntry("Samantha", 50)
o_game10 = GameEntry("Paskal", 70)
o_game11 = GameEntry("Ruby", 56)
o_game12 = GameEntry("No", 20)

"""
print(o_game.get_name())
print(o_game.get_score())
print(o_game)
"""


class Scoreboard():
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity: int=10):
        """Initialize scoreboard with given maximum capacity
        All entries are initially None."""
        self._capacity = capacity
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k) -> "GameEntry":
        """Return entry at index k"""
        return self._board[k]

    def __str__(self) -> str:
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry: "GameEntry") -> None:
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board is not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score drops from list
                self._n += 1  # so overall number increases

            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]  # shift entry from j-1 to j
                j -= 1  # decrement j

            self._board[j] = entry  # when done, add new entry


o_score = Scoreboard()
print(o_score)
o_score.add(o_game)
o_score.add(o_game2)
o_score.add(o_game3)
o_score.add(o_game4)
o_score.add(o_game5)
o_score.add(o_game6)
o_score.add(o_game7)
o_score.add(o_game8)
o_score.add(o_game9)
o_score.add(o_game10)
o_score.add(o_game11)
o_score.add(o_game12)
print(o_score)
