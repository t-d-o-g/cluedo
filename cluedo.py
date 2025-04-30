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
        rand_rooms = list(GameObjects.rooms.keys())
        random.shuffle(rand_rooms)

        for room in rand_rooms:
            if GameObjects.weapons:
                weapon = GameObjects.weapons.pop()
                GameObjects.rooms[room].insert(2, weapon)
            print(f'Room: {room}, Weapon: {weapon}')

        case_file_suspect = GameObjects.suspect_cards.pop(0)
        case_file_weapon = GameObjects.weapon_cards.pop(0)
        case_file_room = GameObjects.room_cards.pop(0)

        GameObjects.envelope.append(case_file_room)
        GameObjects.envelope.append(case_file_weapon)
        GameObjects.envelope.append(case_file_suspect)

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
            command=lambda: self.button_click(
                button['text'])
        )
        return button

    def button_click(self, room):
        print(f'Miss Scarlett is in the {room}.')
        self.close_window()

    def close_window(self):
        self.destroy()

    def player_suggestion(self, player):
        suggestion = []
        rooms = {
            '1': 'kitchen',
            '2': 'ballroom',
            '3': 'conservatory',
            '4': 'billiard room',
            '5': 'dining room',
            '6': 'library',
            '7': 'lounge',
            '8': 'hall',
            '9': 'study'
        }
        print(f'Miss Scarlett, make a suggestion.')
        print('1 - Kitchen')
        print('2 - Ballroom')
        print('3 - Conservatory')
        print('4 - Billiard Room')
        print('5 - Dining Room')
        print('6 - Library')
        print('7 - Lounge')
        print('8 - Hall')
        print('9 - Study')
        while True:
            room_answer = int(input('Which room did the murder take place in? '))
            if 1 <= room_answer <= 9:
                break
            else:
                print("Enter a number between 1 and 9")
        suggestion.append(rooms[str(room_answer)])
        weapons = {
            '1': 'candlestick',
            '2': 'knife',
            '3': 'lead pipe',
            '4': 'pistol',
            '5': 'rope',
            '6': 'wrench'
        }
        print('1 - Candlestick')
        print('2 - knife')
        print('3 - lead pipe')
        print('4 - pistol')
        print('5 - rope')
        print('6 - wrench')
        while True:
            weapon_answer = int(input('Which weapon did the murderer use? '))
            if 1 <= weapon_answer <= 6:
                break
            else:
                print("Enter a number between 1 and 6")
        suggestion.append(weapons[str(weapon_answer)])
        suspects = {
            '1': 'miss scarlet',
            '2': 'col mustard',
            '3': 'mrs. white',
            '4': 'mr. green',
            '5': 'mrs. peacock',
            '6': 'prof plum'
        }
        print('1 - Miss Scarlet')
        print('2 - Col Mustard')
        print('3 - Mrs. White')
        print('4 - Mr. Green')
        print('5 - Mrs. Peacock')
        print('6 - Prof Plum')
        while True:
            suspect_answer = int(input('Who do you suspect committed the murderer? '))
            if 1 <= suspect_answer <= 6:
                break
            else:
                print("Enter a number between 1 and 6")
        suggestion.append(suspects[str(suspect_answer)])
        return suggestion

    def check_envelope(self, suggestion):
        if (suggestion == GameObjects.envelope):
            print('\nMiss Scarlett you have solved the mystery!')
        else:
            print('\nSorry Miss Scarlett, according to the case file:')
            print(f'* The murder took place in the {GameObjects.envelope[0]}')
            print(f'* The weapon used was a {GameObjects.envelope[1]}')
            print(f'* And the murderer is {GameObjects.envelope[2]}!')


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
            text='Miss Scarlett, select a room to inspect.',
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
    cluedo.deal_cards(player_cards)
    print('Miss Scarlett, select a room to inspect.')
    cluedo.arrange_game_board()
    cluedo.display_game(cluedo.board)

    cluedo.mainloop()

    suggestion = cluedo.player_suggestion(GameObjects.suspects['Miss Scarlet'])
    cluedo.check_envelope(suggestion)


if __name__ == '__main__':
    player_cards = [
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    main()
