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
        'Colonel Mustard': 'yellow',
        'Mrs. White': 'white',
        'Mr. Green': 'green',
        'Mrs. Peacock': 'blue',
        'Profesor Plum': 'purple',
    }

    current_player = 'miss scarlet'

    player_cards = {
        'miss scarlet': [],
        'colonel mustard': [],
        'mrs. white': [],
        'mr. green': [],
        'mrs. peacock': [],
        'profesor plum': [],
    }

    player_suggestions = {
        'miss scarlet': [],
        'colonel mustard': [],
        'mrs. white': [],
        'mr. green': [],
        'mrs. peacock': [],
        'profesor plum': [],
    }

    player_refutations = {
        'miss scarlet': [],
        'colonel mustard': [],
        'mrs. white': [],
        'mr. green': [],
        'mrs. peacock': [],
        'profesor plum': [],
    }

    player_deductions = {
        'miss scarlet': [],
        'colonel mustard': [],
        'mrs. white': [],
        'mr. green': [],
        'mrs. peacock': [],
        'profesor plum': [],
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
                    self.player_deductions[key].append(card)
            i += 1
        self.print_detective_notes()

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

    def button_click(self):
        self.close_window()

    def close_window(self):
        self.withdraw()

    def open_window(self):
        self.deiconify()

    def destroy_window(self):
        self.destroy()

    def update_display_title(self, title):
        self.display.config(text=title)
        self.update()

    def make_suggestion(self, room):
        self.close_window()
        accusation = self.make_accusation()
        if accusation == 3:
            print(
                f'The murder was committed in the {GameObjects.envelope[0]} with the {GameObjects.envelope[1]} by {GameObjects.envelope[2].title()}.')
            self.destroy_window()
            return
        room = room.split(' (', 1)[0].lower()
        suspects = {
            '1': 'miss scarlet',
            '2': 'colonel mustard',
            '3': 'mrs. white',
            '4': 'mr. green',
            '5': 'mrs. peacock',
            '6': 'profesor plum'
        }
        while True:
            suspect_answer = int(
                input('\nWho do you suspect committed the murderer? \n'
                      '1 - Miss Scarlet \n'
                      '2 - Colonel Mustard \n'
                      '3 - Mrs. White \n'
                      '4 - Mr. Green \n'
                      '5 - Mrs. Peacock \n'
                      '6 - Profesor Plum \n'
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
        suggestion = (room, weapon, suspect)

        if accusation:
            print(
                f"\n{self.current_player.title()}: I accuse {suspect.title()} of commiting the crime in the {room} with the {weapon}.\n")
            self.check_envelope(suggestion)
        else:
            print(
                f"\n{self.current_player.title()}: I suggest the crime was committed in the {room} by {suspect.title()} with the {weapon}.\n")
            self.player_suggestions[self.current_player.lower()].append(
                suggestion)
            self.suspect_refutation()
            return suggestion

    def refute(self, player, item):
        preposition = 'in the'
        if item in GameObjects.weapon_cards:
            preposition = 'with the'
        elif item in GameObjects.suspect_cards:
            preposition = 'by'
            item = item.title()

        print(
            f'{player.title()}: I can say without a doubt the murder was not committed {preposition} {item}.\n')

    def print_detective_notes(self,):
        self.player_deductions[self.current_player.lower()].extend(
            x for x in self.player_refutations[self.current_player.lower()]
            if x not in self.player_deductions[self.current_player.lower()])
        print('-----------------------------------------------')
        print(f'{self.current_player.title()} Detective Notes:')
        print('-----------------------------------------------')
        print(
            f'Cards: {self.player_cards[self.current_player.lower()]}')
        print(
            f'Suggestions: {self.player_suggestions[self.current_player.lower()]}')
        print(
            f'Refutations: {self.player_refutations[self.current_player.lower()]}')
        print(
            f'Deductions: {self.player_deductions[self.current_player.lower()]}')
        print('-----------------------------------------------')

    def suspect_refutation(self):
        suggestion = self.player_suggestions[self.current_player.lower()][-1]
        match = False
        current_player_cards = self.player_cards.pop(
            self.current_player.lower())
        for player in self.player_cards:
            if match:
                break
            for item in suggestion:
                if item in self.player_cards[player]:
                    match = True
                    if match:
                        self.refute(player, item)
                        self.player_refutations[self.current_player.lower()].append(
                            item)
                        break
        if not match:
            accusation = self.make_suggestion_accusation()
            if accusation:
                self.check_envelope(
                    self.player_suggestions[self.current_player.lower()][-1])
                return

        self.player_cards[self.current_player] = current_player_cards
        self.current_player = next(iter(self.player_cards))

        self.print_detective_notes()
        self.update_display_title(
            f'{self.current_player.title()}, select a room to inspect.')
        self.open_window()

    def make_accusation(self):
        while True:
            make_accusation = int(
                input(f'\n{self.current_player.title()}, would you like to make a suggestion, accusation, or quit?\n'
                      '1 - Suggestion\n'
                      '2 - Accusation\n'
                      '3 - Quit \n'
                      ))
            if 1 <= make_accusation <= 3:
                break
            else:
                print("\nEnter a number between 1 and 3.\n")
        if make_accusation == 2:
            return True
        elif make_accusation == 1:
            return False

        return make_accusation

    def make_suggestion_accusation(self):
        while True:
            make_accusation = int(
                input(f'{self.current_player.title()}, it seems that nobody can refute your suggestion, would you like to make an accusation?\n'
                      '1 - Yes\n'
                      '2 - No\n'
                      ))
            if 1 <= make_accusation <= 2:
                break
            else:
                print("\nEnter the number 1 or 2.\n")
        if make_accusation == 1:
            return True
        elif make_accusation == 2:
            return False

        return make_accusation

    def check_envelope(self, accusation):
        print(f'\nEnvelope: {GameObjects.envelope}')
        alibi = f'I could not have committed the murder because'
        if (accusation == GameObjects.envelope):
            print(f'\n{self.current_player.title()} you have found the murderer!')
        else:
            for item in accusation:
                if item not in GameObjects.envelope:
                    if item in GameObjects.weapon_cards:
                        alibi += f' I don\'t own a {item}.'
                    elif item in GameObjects.room_cards:
                        alibi += f' I was not in the {item} at that time.'
                    elif item in GameObjects.suspect_cards:
                        alibi += f' The DNA test proves it was not me.'
            print(f'\n{accusation[2].title()}: {alibi}')
        self.destroy_window()

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
    # print(f'Envelope: {GameObjects.envelope}')
    cluedo.arrange_game_board()
    cluedo.display_game(cluedo.board)

    w = 800
    h = 1000
    ws = cluedo.winfo_screenwidth()
    hs = cluedo.winfo_screenheight()
    x = (ws/2) - (w/2) + 800
    y = (hs/2) - (h/2) - 200
    cluedo.geometry('%dx%d+%d+%d' % (w, h, x, y))
    cluedo.mainloop()


if __name__ == '__main__':
    main()
