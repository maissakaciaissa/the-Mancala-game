import copy

# Classe représentant le plateau du jeu Mancala
class MancalaBoard:
    def __init__(self):
        self.board = {**{chr(i): 4 for i in range(65, 77)}, "P1": 0, "P2": 0}
        self.player1_pits = tuple(chr(i) for i in range(65, 71))  # A-F
        self.player2_pits = tuple(chr(i) for i in range(71, 77))  # G-L
        self.stores = {"P1": "P1", "P2": "P2"}
        self.opposite = {**dict(zip(self.player1_pits, reversed(self.player2_pits))),
                         **dict(zip(self.player2_pits, reversed(self.player1_pits)))}
        self.next_pit = {**{chr(i): chr(i + 1) for i in range(65, 76)},
                         **{"F": "P1", "L": "P2", "P1": "G", "P2": "A"}}

    def possible_moves(self, player):
        pits = self.player1_pits if player == "P1" else self.player2_pits
        return [pit for pit in pits if self.board[pit] > 0]

    def do_move(self, player, pit):
        seeds = self.board[pit]
        self.board[pit] = 0
        current = pit
        while seeds > 0:
            current = self.next_pit[current]
            if current == self.stores["P2" if player == "P1" else "P1"]:
                continue
            self.board[current] += 1
            seeds -= 1
        if current in (self.player1_pits if player == "P1" else self.player2_pits) and self.board[current] == 1:
            opposite = self.opposite[current]
            self.board[self.stores[player]] += self.board[opposite] + 1
            self.board[current] = self.board[opposite] = 0
        return current

    def is_game_over(self):
        return all(self.board[pit] == 0 for pit in self.player1_pits) or \
               all(self.board[pit] == 0 for pit in self.player2_pits)

    def collect_remaining_seeds(self):
        for pit in self.player1_pits:
            self.board["P1"] += self.board[pit]
            self.board[pit] = 0
        for pit in self.player2_pits:
            self.board["P2"] += self.board[pit]
            self.board[pit] = 0

class Game:
    def __init__(self):
        self.state = MancalaBoard()
        self.player_side = {"HUMAN": "P1", "COMPUTER": "P2"}

    def game_over(self):
        if self.state.is_game_over():
            self.state.collect_remaining_seeds()
            return True
        return False

    def find_winner(self):
        return max(("P1", self.state.board["P1"]), ("P2", self.state.board["P2"]), key=lambda x: x[1])

    def evaluate(self):
        computer_store = self.state.board[self.state.stores[self.player_side["COMPUTER"]]]
        human_store = self.state.board[self.state.stores[self.player_side["HUMAN"]]]
        return computer_store - human_store

    def computer_vs_computer_heuristic(self, player, pit):
        # Nouvelle heuristique : prioriser les coups offrant un tour supplémentaire ou capturant le plus de graines
        board_copy = copy.deepcopy(self.state)
        last_pit = board_copy.do_move(player, pit)
        score_gain = board_copy.board[self.state.stores[player]] - self.state.board[self.state.stores[player]]
        extra_turn = 1 if (player == "P1" and last_pit == "P1") or (player == "P2" and last_pit == "P2") else 0
        return score_gain + extra_turn * 10

# Fonction de Minimax avec élagage alpha-bêta
def MinimaxAlphaBetaPruning(game, player, depth, alpha, beta, heuristic_mode="default"):
    if game.game_over() or depth == 0:
        best_value = game.evaluate()
        return best_value, None

    if player == "MAX":
        best_value = float('-inf')
        best_pit = None
        for pit in game.state.possible_moves(game.player_side["COMPUTER"]):
            child_game = copy.deepcopy(game)
            child_game.state.do_move(game.player_side["COMPUTER"], pit)
            value, _ = MinimaxAlphaBetaPruning(child_game, "MIN", depth - 1, alpha, beta, heuristic_mode)
            if value > best_value:
                best_value = value
                best_pit = pit
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value, best_pit

    else:
        best_value = float('inf')
        best_pit = None
        for pit in game.state.possible_moves(game.player_side["HUMAN"]):
            child_game = copy.deepcopy(game)
            child_game.state.do_move(game.player_side["HUMAN"], pit)
            value, _ = MinimaxAlphaBetaPruning(child_game, "MAX", depth - 1, alpha, beta, heuristic_mode)
            if value < best_value:
                best_value = value
                best_pit = pit
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_pit
class Play:
    def __init__(self):
        self.game = Game()

    def choose_starting_player(self):
        print("Who should start first?")
        print("1. Human")
        print("2. Computer")
        choice = input("Enter 1 or 2: ").strip()
        while choice not in ('1', '2'):
            choice = input("Invalid choice. Enter 1 for Human or 2 for Computer: ").strip()
        return "HUMAN" if choice == '1' else "COMPUTER"

    def human_turn(self):
        print("Your turn. Possible pits:", self.game.state.possible_moves(self.game.player_side["HUMAN"]))
        pit = input("Choose a pit: ").strip().upper()
        while pit not in self.game.state.possible_moves(self.game.player_side["HUMAN"]):
            pit = input("Invalid move. Choose another pit: ").strip().upper()
        self.game.state.do_move(self.game.player_side["HUMAN"], pit)

    def computer_turn(self):
        _, best_move = MinimaxAlphaBetaPruning(self.game, "MAX", depth=3, alpha=float('-inf'), beta=float('inf'))
        self.game.state.do_move(self.game.player_side["COMPUTER"], best_move)
        print(f"Computer chose pit {best_move}")

    def play_human_vs_computer(self):
        starting_player = self.choose_starting_player()
        current_player = starting_player

        while not self.game.game_over():
            if current_player == "HUMAN":
                self.human_turn()
                current_player = "COMPUTER"
            else:
                self.computer_turn()
                current_player = "HUMAN"
        
        winner, score = self.game.find_winner()
        print(f"Game Over! Winner: {winner} with score {score}")


    def computer_vs_computer_turn(self, player):
        possible_moves = self.game.state.possible_moves(player)
        best_move = max(possible_moves, key=lambda pit: self.game.computer_vs_computer_heuristic(player, pit))
        self.game.state.do_move(player, best_move)

    def play_computer_vs_computer(self):
        while not self.game.game_over():
            self.computer_vs_computer_turn("P1")
            if self.game.game_over():
                break
            self.computer_vs_computer_turn("P2")
        winner, score = self.game.find_winner()
        print(f"Game Over! Winner: {winner} with score {score}")

