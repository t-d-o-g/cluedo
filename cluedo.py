import random
from gameobjects import GameObjects
from gameboard import GameBoard
import tkinter as tk

class Cluedo:


    def game_setup():
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


    def deal_cards(players):
        i = 0
        while len(GameObjects.cards) > 0:
            card = GameObjects.cards.pop(0)
            player_cards[i % len(players)].append(card)
            i += 1

    def roll_die():
        GameObjects.die = random.randint(1,6) 

    def player_move(player):
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



if __name__ == "__main__":
    cluedo = Cluedo
    player_cards = [
        [],
        [],
        [],
        [],
        [],
        [],
    ]

    cluedo.game_setup()
    cluedo.deal_cards(player_cards)
    # print('Col Mustard cards: ', player_cards[1])
    # print('Mrs. White: ', player_cards[2])
    # print('Mr. Green: ',  player_cards[3])
    # print('Mrs. Peacock: ', player_cards[4])
    # print('Prof Plum: ', player_cards[5])
    # print('Envelope: ', GameObjects.envelope)

    print(f'Miss Scarlett\'s cards: {player_cards[0]}')
    cluedo.player_move(GameObjects.suspects['Miss Scarlet'])
    GameBoard.arrange_game_board()
    root = tk.Tk()
    root.title("Cluedo")
    GameBoard.display_game(GameBoard.board, root)
    root.mainloop()
