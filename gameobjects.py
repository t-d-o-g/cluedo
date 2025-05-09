class GameObjects:
    """
    Class used to store game object related data
    """

    suspect_cards = [
        'miss scarlet',
        'colonel mustard',
        'mrs. white',
        'mr. green',
        'mrs. peacock',
        'profesor plum',
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
        'Miss Scarlet': [0, 6],
        'Colonel Mustard': [3, 9],
        'Mrs. White': [11, 5],
        'Mr. Green': [11, 3],
        'Mrs. Peacock': [9, 0],
        'Profesor Plum': [4, 0],
    }

    rooms = {
        'Kitchen': [10, 7],
        'Ballroom': [10, 4],
        'Conservatory': [10, 1],
        'Billiard Room': [7, 1],
        'Dining Room': [5, 7],
        'Library': [5, 1],
        'Lounge': [1, 7],
        'Hall': [1, 4],
        'Study': [1, 1]
    }

    envelope = ()
    cards = []
