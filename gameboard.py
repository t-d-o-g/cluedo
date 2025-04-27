import tkinter as tk
from gameobjects import GameObjects


class GameBoard:

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

    def arrange_game_board():
        for suspect in GameObjects.suspects:
            GameBoard.board[GameObjects.suspects[suspect][0]
                            ][GameObjects.suspects[suspect][1]] = suspect

        for room in GameObjects.rooms:
            if (len(GameObjects.rooms[room]) <= 2):
                GameBoard.board[GameObjects.rooms[room][0]
                                ][GameObjects.rooms[room][1]] = room
            else:
                GameBoard.board[GameObjects.rooms[room][0]][GameObjects.rooms[room]
                                                            [1]] = f'{room} ({GameObjects.rooms[room][2]})'

    def display_game(game_data, root):
        rows = len(game_data)
        cols = len(game_data[0])

        for i in range(rows):
            for j in range(cols):
                is_room = game_data[i][j].split(
                    ' (')[0] in GameObjects.rooms

                if game_data[i][j] in GameObjects.suspects:
                    bg_color = GameBoard.color_map[game_data[i][j]]
                elif is_room:
                    bg_color = 'gray'
                else:
                    bg_color = 'light gray'

                entry = tk.Button(
                    root, text=game_data[i][j], wraplength=100, relief="solid", disabledforeground="black", bg=bg_color)

                if is_room:
                    entry.config(state=tk.NORMAL)
                else:
                    entry.config(state=tk.DISABLED)

                entry.grid(row=i, column=j)
                entry.config(width=15, height=2)
