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
    player_cards = {
        'miss scarlet': [],
        'col mustard': [],
        'mrs. white': [],
        'mr. green': [],
        'mrs. peacock': [],
        'prof plum': [],
    }

    current_player = 'Miss Scarlet'
    suggestions = [] 
    refutations = []

    def game_setup(self):
        random.shuffle(GameObjects.suspect_cards)
        random.shuffle(GameObjects.weapon_cards)
        random.shuffle(GameObjects.room_cards)
        random.shuffle(GameObjects.weapons)
        rand_rooms = list(GameObjects.rooms.keys())
        random.shuffle(rand_rooms)

        for room in rand_rooms:
            if GameObjects.weapons:
                weapon = GameObjects.weapons.pop()
                GameObjects.rooms[room].insert(2, weapon)

        case_file_suspect = GameObjects.suspect_cards.pop(0)
        case_file_weapon = GameObjects.weapon_cards.pop(0)
        case_file_room = GameObjects.room_cards.pop(0)

        GameObjects.envelope = (
            case_file_room, case_file_weapon, case_file_suspect)

        GameObjects.cards.extend(GameObjects.suspect_cards)
        GameObjects.cards.extend(GameObjects.weapon_cards)
        GameObjects.cards.extend(GameObjects.room_cards)
        random.shuffle(GameObjects.cards)

    def deal_cards(self):
        i = 0
        while len(GameObjects.cards) > 0:
            for key in self.player_cards:
                if GameObjects.cards:
                    card = GameObjects.cards.pop(0)
                    self.player_cards[key].append(card)
            i += 1
        print("player cards:")
        print(self.player_cards)

    def create_button(self, frame, text, bg_color):
        button = tk.Button(
            master=frame,
            text=text,
            wraplength=50,
            relief='solid',
            disabledforeground='black',
            fg='black',
            bg=bg_color,
            width=4,
            height=3,
            command=lambda: self.make_suggestion(
                button['text'])
        )
        return button

    def button_click(self, room):
        self.close_window()

    def close_window(self):
        self.destroy()

    def make_suggestion(self, room):
        self.close_window()
        room = room.split(' (', 1)[0].lower()
        suspects = {
            '1': 'miss scarlet',
            '2': 'col mustard',
            '3': 'mrs. white',
            '4': 'mr. green',
            '5': 'mrs. peacock',
            '6': 'prof plum'
        }
        while True:
            suspect_answer = int(
                input('\nWho do you suspect committed the murderer? \n'
                      '1 - Miss Scarlet \n'
                      '2 - Col Mustard \n'
                      '3 - Mrs. White \n'
                      '4 - Mr. Green \n'
                      '5 - Mrs. Peacock \n'
                      '6 - Prof Plum \n'
                      ))
            if 1 <= suspect_answer <= 6:
                break
            else:
                print("\nEnter a number between 1 and 6.\n")
        suspect = suspects[str(suspect_answer)]

        weapons = {
            '1': 'candlestick',
            '2': 'knife',
            '3': 'lead pipe',
            '4': 'pistol',
            '5': 'rope',
            '6': 'wrench'
        }
        while True:
            weapon_answer = int(input('\nWhich weapon did the murderer use? \n'
                                      '1 - Candlestick \n'
                                      '2 - Knife \n'
                                      '3 - Lead Pipe \n'
                                      '4 - Pistol \n'
                                      '5 - Rope \n'
                                      '6 - Wrench \n'
                                      ))
            if 1 <= weapon_answer <= 6:
                break
            else:
                print("\nEnter a number between 1 and 6.\n")
        weapon = weapons[str(weapon_answer)]
        print(
            f"\n{self.current_player}: I suggest the crime was commited in the {room} by {suspect} with the {weapon}.\n")
        suggestion = (self.current_player, room, weapon, suspect)
        self.suggestions.append(suggestion)
        return suggestion

    def suspect_refutation(self):
        suggestion = self.suggestions[0]
        if (suggestion[1:] == GameObjects.envelope):
            print(f'{self.current_player} you have solved the mystery!')
        else:
            print(
                f'{suggestion[3]}: I could not have committed the murder because:')
            for item in suggestion[:3]:
                if item in self.player_cards[suggestion[3]]:
                    print(f'I can say for sure it was not {item}.')
                else:
                    print('No I can not.')

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
            text=f'{self.current_player}, select a room to inspect.',
            font=font.Font(size=10, weight='bold'),
        )
        self.display.pack()

    def display_game(self, game_data):
        rows = len(game_data)
        cols = len(game_data[0])
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        i = 0
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

                button = self.create_button(
                    grid_frame, game_data[row][col], bg_color)

                self.cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsew'
                )

                if is_room:
                    button.config(state=tk.NORMAL)
                else:
                    button.config(state=tk.DISABLED)
                i += 1


def main():
    cluedo = Cluedo()

    cluedo.game_setup()
    cluedo.deal_cards()
    print("Envelope:")
    print(GameObjects.envelope)
    cluedo.arrange_game_board()
    cluedo.display_game(cluedo.board)

    cluedo.mainloop()

    cluedo.suspect_refutation()


if __name__ == '__main__':
    main()
