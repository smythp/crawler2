## Lexicon for parser

tokens = {
    'directions':[
        'NORTH',
        'SOUTH',
        'EAST',
        'WEST',
        'NORTHWEST',
        'NORTHEAST',
        'SOUTHEAST',
        'SOUTHWEST',
        'UP',
        'DOWN',
        'IN',
        'OUT',
        'EXIT',
        'N',
        'S',
        'E',
        'W',
        'U',
        'D',
        'NW',
        'NE',
        'SE',
        'NW',
        ],
    'verbs':[
        'QUIT',
        'GO',
        'L',
        'LOOK',
        'RUN',
        'WALK',
        'EAT',
        'KILL',
        ],
    'nouns':
     [
        'BEAR',
        'PRINCESS',
        ],
    'filler':[
        'THE',
        'AND',
        'OF',
        'A',
        'AN',],
    }


## Synonym dictionary

synonyms = {
    'L': 'LOOK',
    'SCRUTINIZE': 'LOOK',
    'EXAMINE': 'LOOK',
    'X': 'LOOK',
    'NORTH': 'N',
    'SOUTH': 'S',
    'EAST':'E',
    'WEST':'W',
    'UP':'U',
    'DOWN':'D',
    'WALK':'GO',
    'MOVE':'GO',
    'RUN':'GO',
    'AMBLE':'GO',
    }
