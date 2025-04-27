
class GameObjects:
    suspect_cards = [
        'miss scarlet',
        'col mustard',
        'mrs white',
        'mr green',
        'mrs peacock',
        'prof plum',
    ]

    weapon_cards = [
        'candlestick',
        'knife',
        'lead pipe',
        'pistol',
        'rope',
        'wrench',
    ]

    room_cards = [
        'kitchen',
        'ballroom',
        'conservatory',
        'dining room',
        'billiard room',
        'library',
        'lounge',
        'hall',
        'study'
    ]

    weapons = [
        'candlestick',
        'knife',
        'lead pipe',
        'pistol',
        'rope',
        'wrench',
    ]

    suspects = {
        'Miss Scarlet': [0,6],
        'Col Mustard': [3,9],
        'Mrs. White': [11,5],
        'Mr. Green': [11,3],
        'Mrs. Peacock': [9,0],
        'Prof Plum': [4,0],
    }

    rooms = {
        'Kitchen': [10,7],
        'Ballroom': [10,4],
        'Conservatory': [10,1],
        'Billiard Room': [7,1],
        'Dining Room': [5,7],
        'Library': [5,1],
        'Lounge': [1,7],
        'Hall': [1,4],
        'Study': [1,1]
    }

    die = 1 
    envelope = []
    cards = []