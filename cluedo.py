import random
import tkinter as tk
from tkinter import font
from gameobjects import GameObjects


class Cluedo(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Cluedo")
        self.cells = {}
        self.create_board_display()

    board = [
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', 'Case File', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '', ''],
    ]

    color_map = {
        'Miss Scarlet': 'red',
        'Col Mustard': 'yellow',
        'Mrs. White': 'white',
        'Mr. Green': 'green',
        'Mrs. Peacock': 'blue',
        'Prof Plum': 'purple',
    }

    def game_setup(self):
        random.shuffle(GameObjects.suspect_cards)
        random.shuffle(GameObjects.weapon_cards)
        random.shuffle(GameObjects.room_cards)
        random.shuffle(GameObjects.weapons)

        for room in GameObjects.rooms:
            if GameObjects.weapons:
                weapon = GameObjects.weapons.pop()
                GameObjects.rooms[room].insert(2, weapon)

        case_file_suspect = GameObjects.suspect_cards.pop(0)
        case_file_weapon = GameObjects.weapon_cards.pop(0)
        case_file_room = GameObjects.room_cards.pop(0)

        GameObjects.envelope.append(case_file_suspect)
        GameObjects.envelope.append(case_file_weapon)
        GameObjects.envelope.append(case_file_room)

        GameObjects.cards.extend(GameObjects.suspect_cards)
        GameObjects.cards.extend(GameObjects.weapon_cards)
        GameObjects.cards.extend(GameObjects.room_cards)
        random.shuffle(GameObjects.cards)

    def deal_cards(self, players):
        i = 0
        while len(GameObjects.cards) > 0:
            card = GameObjects.cards.pop(0)
            player_cards[i % len(players)].append(card)
            i += 1

    def roll_die():
        GameObjects.die = random.randint(1, 6)

    def player_move(self, player):
        print(f'Miss Scarlett, select a room to inspect.')
        # print('0 - Kitchen')
        # print('1 - Ballroom')
        # print('2 - Conservatory')
        # print('3 - Billiard Room')
        # print('4 - Dining Room')
        # print('5 - Library')
        # print('6 - Lounge')
        # print('7 - Hall')
        # print('8 - Study')

    def arrange_game_board(self):
        for suspect in GameObjects.suspects:
            Cluedo.board[GameObjects.suspects[suspect][0]
                            ][GameObjects.suspects[suspect][1]] = suspect

        for room in GameObjects.rooms:
            if (len(GameObjects.rooms[room]) <= 2):
                Cluedo.board[GameObjects.rooms[room][0]
                                ][GameObjects.rooms[room][1]] = room
            else:
                Cluedo.board[GameObjects.rooms[room][0]][GameObjects.rooms[room]
                                                            [1]] = f'{room} ({GameObjects.rooms[room][2]})'

    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Select a room.",
            font=font.Font(size=10, weight="bold"),
        )
        self.display.pack()

    def display_game(self, game_data):
        rows = len(game_data)
        cols = len(game_data[0])
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        for row in range(rows):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(cols):
                is_room = game_data[row][col].split(
                    ' (')[0] in GameObjects.rooms

                if game_data[row][col] in GameObjects.suspects:
                    bg_color = Cluedo.color_map[game_data[row][col]]
                elif is_room:
                    bg_color = 'gray'
                else:
                    bg_color = 'light gray'

                button = tk.Button(
                    master=grid_frame,
                    text=game_data[row][col],
                    # font=font.Font(size=36, weight="bold"),
                    wraplength=50,
                    relief="solid",
                    disabledforeground="black",
                    fg='black',
                    bg=bg_color,
                    width=4,
                    height=3,
                )
                self.cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

                if is_room:
                    button.config(state=tk.NORMAL)
                else:
                    button.config(state=tk.DISABLED)


def main():
    cluedo = Cluedo()

    cluedo.game_setup()
    cluedo.deal_cards(player_cards)
    cluedo.player_move(GameObjects.suspects['Miss Scarlet'])
    cluedo.arrange_game_board()
    cluedo.display_game(cluedo.board)

    cluedo.mainloop()


if __name__ == "__main__":
    player_cards = [
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    main()
