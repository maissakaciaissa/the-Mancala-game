mimi
mimi8435
Invisible

mimi — Yesterday at 13:35
Same thing happened f google colan
👍 — Yesterday at 13:42
Ok
👌
mimi — Yesterday at 13:56
sarah doka nti htns9i ta3k?
👍 — Yesterday at 13:56
Yep wla nkhalih w nhdrou 3la had le truc f rapport
Car haja mliha
mimi — Yesterday at 13:58
ns9soh doka ?
👍 — Yesterday at 13:58
Yep
Ana ha ndihol chwiya retard car 3yit mn se
mimi — Yesterday at 13:59
okey ida s9sito n9olk
👍 — Yesterday at 13:59
Ok
mimi — Yesterday at 14:03
sarah diri reminder f discord
makayn hata whd apart ana
👍 — Yesterday at 14:03
Ok
Mdr nchlh ydkhlou
mimi — Yesterday at 14:09
inshallah
mimi — Yesterday at 14:21
@👍  sarah kifch derti f monde reel mfhmtch the push
👍 — Yesterday at 14:29
Kayan t3e dna
W kayan t3e english text
mimi — Yesterday at 14:30
had function  u are generating had type of tests and thbsi time and everything ?
Image
👍 — Yesterday at 14:41
Non hada y9ra fichier adn.txt
mimi — Yesterday at 14:42
YAKHO
f les vacances nchlh ndir hada
👍 — Yesterday at 14:42
Ok 👌
You are free
mimi — Yesterday at 14:43
khlas raho 9al on limite pas
👍 — Yesterday at 14:43
👌👌👌
mimi — Yesterday at 14:44
yak 9al complexite O(n)
👍 — Yesterday at 14:45
I dont know manich nsm3e fih 😭
mimi — Yesterday at 14:45
okey thanks
annonce f discord travail2+3 le 3 janvier
serie le 22
👍 — Yesterday at 14:45
Oui bon houwa ha yb3t email
mimi — Yesterday at 14:46
ah okey haya bet
mimi — Yesterday at 17:37
@👍  SARAH
👍 — Yesterday at 17:37
oui
mimi — Yesterday at 17:37
stp f tp sys yak prof 9alna zido hadak tampon
👍 — Yesterday at 17:37
yep
mimi — Yesterday at 17:38
 struct tampon {
    int q;    // Queue pointer (next empty in tampon)
    int cpt;  // Counter for the number of items in the tampon
    struct Tfmissions {
        int camion_id;         // Truck identifier
        int mission_status;    // Mission status (5 if finished)
        int consomation_recente; // Recent consumption
    } tabmission[R];
haka?
sarah
so tampon ywali fil q, t, cpt and tmission?  hadi haka tani
👍 — Yesterday at 17:39
nonnn je pense pas haka
mimi — Yesterday at 17:40
okeyyy
👍 — Yesterday at 18:37
tmo rahi ghlta machi haka 9al l prof
👍 — Today at 08:08
import copy

# Classe représentant le plateau du jeu Mancala
class MancalaBoard:
    def __init__(self):
        self.board = {**{chr(i): 4 for i in range(65, 77)}, "P1": 0, "P2": 0}
Expand
sol2.py
8 KB
import tkinter as tk
from sol2 import Game, MinimaxAlphaBetaPruning

class MancalaGUI:
    def __init__(self, root):
        self.root = root
Expand
sol2gui.py
11 KB
mimi — Today at 08:59
import copy

# Classe représentant le plateau du jeu Mancala
class MancalaBoard:
    def __init__(self):
        self.board = {**{chr(i): 4 for i in range(65, 77)}, "P1": 0, "P2": 0}
Expand
p4.py
8 KB
import tkinter as tk
from p4 import Game, MinimaxAlphaBetaPruning

class MancalaGUI:
    def __init__(self, root):
        self.root = root
Expand
gui.py
11 KB
mimi — Today at 09:15
Image
mimi — Today at 09:30
import tkinter as tk
from p4 import Game, MinimaxAlphaBetaPruning

class MancalaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mancala Game")
        self.root.geometry("700x650")
        self.game = None

        # Define colors and style
        self.bg_color = "#FFF5F8"  # Soft pinkish background
        self.button_color = "#FFC3E6"  # Light pink for buttons
        self.store_color = "#FFD4E5"  # Soft rosy pink for stores
        self.disabled_color = "#FFE0EC"  # Light pastel pink for disabled buttons
        self.text_color = "#6A1B78"  # Deep purple for text

        # Font for labels and buttons
        self.title_font = ("Georgia", 26, "bold")
        self.font = ("Georgia", 16)

        # Main frame for background color
        self.root.config(bg=self.bg_color)

        # Winner label
        self.winner_label = tk.Label(
            self.root, text="", font=("Georgia", 20, "bold"), bg=self.bg_color, fg="dark red"
        )
        self.winner_label.pack(pady=10)

        # Initialize GUI
        self.main_menu()

    def main_menu(self):
        """Display the main menu."""
        self.clear_screen()

        tk.Label(
            self.root, text="Welcome to Mancala!", font=self.title_font, bg=self.bg_color, fg=self.text_color
        ).pack(pady=30)

        tk.Button(
            self.root,
            text="Player vs Machine",
            font=self.font,
            bg=self.button_color,
            command=self.start_player_vs_machine,
            width=20,
            height=2,
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Machine vs Machine",
            font=self.font,
            bg=self.button_color,
            command=self.start_machine_vs_machine,
            width=20,
            height=2,
        ).pack(pady=10)

    def start_player_vs_machine(self):
        """Start the Player vs Machine mode."""
        self.game = Game()
        self.winner_label.config(text="")
        self.choose_player_side()

    def start_machine_vs_machine(self):
        """Start the Machine vs Machine mode."""
        self.game = Game()
        self.winner_label.config(text="")
        self.machine_vs_machine()

    def start_game(self, first_player):
        """Start the game based on the chosen starting player."""
        self.game.current_player = first_player
        self.update_board()

        if first_player == "COMPUTER":
            self.root.after(1000, self.computer_turn)

    def choose_player_side(self):
        """Prompt the user to choose their side."""
        self.clear_screen()

        tk.Label(
            self.root, text="Choose Your Side", font=self.title_font, bg=self.bg_color, fg=self.text_color
        ).pack(pady=30)

        play_as_p1_button = tk.Button(
            self.root,
            text="Play as P1",
            font=self.font,
            bg=self.button_color,
            command=lambda: self.setup_game("P1"),
            width=20,
            height=2,
        )
        play_as_p1_button.pack(pady=10)

... (200 lines left)
Collapse
message.txt
11 KB
﻿
import tkinter as tk
from p4 import Game, MinimaxAlphaBetaPruning

class MancalaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mancala Game")
        self.root.geometry("700x650")
        self.game = None

        # Define colors and style
        self.bg_color = "#FFF5F8"  # Soft pinkish background
        self.button_color = "#FFC3E6"  # Light pink for buttons
        self.store_color = "#FFD4E5"  # Soft rosy pink for stores
        self.disabled_color = "#FFE0EC"  # Light pastel pink for disabled buttons
        self.text_color = "#6A1B78"  # Deep purple for text

        # Font for labels and buttons
        self.title_font = ("Georgia", 26, "bold")
        self.font = ("Georgia", 16)

        # Main frame for background color
        self.root.config(bg=self.bg_color)

        # Winner label
        self.winner_label = tk.Label(
            self.root, text="", font=("Georgia", 20, "bold"), bg=self.bg_color, fg="dark red"
        )
        self.winner_label.pack(pady=10)

        # Initialize GUI
        self.main_menu()

    def main_menu(self):
        """Display the main menu."""
        self.clear_screen()

        tk.Label(
            self.root, text="Welcome to Mancala!", font=self.title_font, bg=self.bg_color, fg=self.text_color
        ).pack(pady=30)

        tk.Button(
            self.root,
            text="Player vs Machine",
            font=self.font,
            bg=self.button_color,
            command=self.start_player_vs_machine,
            width=20,
            height=2,
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Machine vs Machine",
            font=self.font,
            bg=self.button_color,
            command=self.start_machine_vs_machine,
            width=20,
            height=2,
        ).pack(pady=10)

    def start_player_vs_machine(self):
        """Start the Player vs Machine mode."""
        self.game = Game()
        self.winner_label.config(text="")
        self.choose_player_side()

    def start_machine_vs_machine(self):
        """Start the Machine vs Machine mode."""
        self.game = Game()
        self.winner_label.config(text="")
        self.machine_vs_machine()

    def start_game(self, first_player):
        """Start the game based on the chosen starting player."""
        self.game.current_player = first_player
        self.update_board()

        if first_player == "COMPUTER":
            self.root.after(1000, self.computer_turn)

    def choose_player_side(self):
        """Prompt the user to choose their side."""
        self.clear_screen()

        tk.Label(
            self.root, text="Choose Your Side", font=self.title_font, bg=self.bg_color, fg=self.text_color
        ).pack(pady=30)

        play_as_p1_button = tk.Button(
            self.root,
            text="Play as P1",
            font=self.font,
            bg=self.button_color,
            command=lambda: self.setup_game("P1"),
            width=20,
            height=2,
        )
        play_as_p1_button.pack(pady=10)

        play_as_p2_button = tk.Button(
            self.root,
            text="Play as P2",
            font=self.font,
            bg=self.button_color,
            command=lambda: self.setup_game("P2"),
            width=20,
            height=2,
        )
        play_as_p2_button.pack(pady=10)

        back_button = tk.Button(
            self.root,
            text="Back",
            font=self.font,
            bg=self.disabled_color,
            command=self.main_menu,
            width=20,
            height=2,
        )
        back_button.pack(pady=20)

    def setup_game(self, side):
        """Set up the game board and initialize player sides."""
        if side == "P1":
            self.game.player_side = {"HUMAN": "P1", "COMPUTER": "P2"}
        else:
            self.game.player_side = {"HUMAN": "P2", "COMPUTER": "P1"}

        self.clear_screen()
        self.create_game_board()

    def create_game_board(self):
        """Create the Mancala game board."""
        # Define the frames for Player 1 and Player 2
        player1_frame = tk.Frame(self.root, bg=self.bg_color)
        player2_frame = tk.Frame(self.root, bg=self.bg_color)

        self.buttons = {}
        self.labels = {}

        # Create Player 1's pits (A, B, C, D, E, F)
        for pit in self.game.state.player1_pits:
            self.buttons[pit] = tk.Button(
                player1_frame,
                text=f"{pit}\n4",
                command=lambda p=pit: self.player_move(p) if self.game.player_side["HUMAN"] == "P1" else None,
                font=self.font,
                width=6,
                height=3,
                bg=self.button_color,
                relief="solid",
            )
            self.buttons[pit].pack(side=tk.LEFT, padx=15)

        # Create Player 2's pits (L, K, J, I, H, G) - Reverse order if human is Player 2
        player2_pits = list(reversed(self.game.state.player2_pits)) if self.game.player_side["HUMAN"] == "P2" else self.game.state.player2_pits
        for pit in player2_pits:
            self.buttons[pit] = tk.Button(
                player2_frame,
                text=f"{pit}\n4",
                command=lambda p=pit: self.player_move(p) if self.game.player_side["HUMAN"] == "P2" else None,
                font=self.font,
                width=6,
                height=3,
                bg=self.disabled_color,
                relief="solid",
            )
            self.buttons[pit].pack(side=tk.LEFT, padx=15)

        # Create Player 1 and Player 2's store labels
        self.labels["P1"] = tk.Label(
            self.root,
            text="P1 Store: 0",
            font=("Georgia", 18),
            bg=self.store_color,
            fg=self.text_color,
            width=20,
            height=2,
            relief="solid",
        )
        self.labels["P1"].pack(pady=20)

        self.labels["P2"] = tk.Label(
            self.root,
            text="P2 Store: 0",
            font=("Georgia", 18),
            bg=self.store_color,
            fg=self.text_color,
            width=20,
            height=2,
            relief="solid",
        )
        self.labels["P2"].pack(pady=20)

        # If the human plays as Player 2, swap the positions of pits and stores
        if self.game.player_side["HUMAN"] == "P2":
            # Re-position Player 1's frame and Player 2's frame
            player1_frame.pack_forget()
            player2_frame.pack_forget()

            # Player 2 pits should be at the bottom and Player 1 pits at the top
            player2_frame.pack(pady=20, side=tk.BOTTOM)
            player1_frame.pack(pady=20, side=tk.TOP)

            # Reposition store labels for Player 1 and Player 2 (Player 2's store at bottom)
            self.labels["P2"].pack(pady=20, side=tk.BOTTOM)
            self.labels["P1"].pack(pady=20, side=tk.TOP)
        else:
            # If Player 1 is human, keep the default layout
            player1_frame.pack(pady=20)
            player2_frame.pack(pady=20)

            # Reposition store labels for Player 1 and Player 2
            self.labels["P1"].pack(pady=20, side=tk.TOP)
            self.labels["P2"].pack(pady=20, side=tk.BOTTOM)

        self.update_board()

    def update_board(self):
        """Update the GUI elements to reflect the current board state."""
        for pit, count in self.game.state.board.items():
            if pit in self.buttons:
                self.buttons[pit]["text"] = f"{pit}\n{count}"
        for store in self.game.state.stores.values():
            self.labels[store]["text"] = f"{store} Store: {self.game.state.board[store]}"

    def enable_player_buttons(self):
        """Enable buttons for the player's valid pits."""
        human_pits = (self.game.state.player1_pits if self.game.player_side["HUMAN"] == "P1"
                      else self.game.state.player2_pits)
        computer_pits = (self.game.state.player2_pits if self.game.player_side["HUMAN"] == "P1"
                         else self.game.state.player1_pits)

        for pit in human_pits:
            if pit in self.game.state.possible_moves(self.game.player_side["HUMAN"]):
                self.buttons[pit]["state"] = tk.NORMAL
                self.buttons[pit]["bg"] = self.button_color
            else:
                self.buttons[pit]["state"] = tk.DISABLED
                self.buttons[pit]["bg"] = self.disabled_color

        for pit in computer_pits:
            self.buttons[pit]["state"] = tk.DISABLED

    def disable_all_buttons(self):
        """Disable all buttons temporarily."""
        for button in self.buttons.values():
            button["state"] = tk.DISABLED

    def player_move(self, pit):
        """Handle player's move."""
        if pit not in self.game.state.possible_moves(self.game.player_side["HUMAN"]):
            self.winner_label.config(text="Invalid Move! Choose a valid pit.")
            return

        self.game.state.do_move(self.game.player_side["HUMAN"], pit)
        self.update_board()

        if self.game.game_over():
            self.end_game()
        else:
            self.disable_all_buttons()
            self.root.after(1000, self.computer_turn)

    def computer_turn(self):
        """Handle computer's move."""
        _, best_move = MinimaxAlphaBetaPruning(
            self.game, "MAX", depth=3, alpha=float('-inf'), beta=float('inf')
        )
        self.game.state.do_move(self.game.player_side["COMPUTER"], best_move)
        self.update_board()

        if self.game.game_over():
            self.end_game()
        else:
            self.enable_player_buttons()

    def end_game(self):
        """Declare winner and end game."""
        self.update_board()
        winner, score = self.game.find_winner()
        self.winner_label.config(text=f"Winner: {winner} with score {score}")

    def clear_screen(self):
        """Clear all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Recreate the winner label after clearing the screen
        self.winner_label = tk.Label(
            self.root, text="", font=("Georgia", 20, "bold"), bg=self.bg_color, fg="dark red"
        )
        self.winner_label.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    gui = MancalaGUI(root)
    root.mainloop()
message.txt
11 KB