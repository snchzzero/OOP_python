class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.score = score
        self.old = old

    def __bool__(self):
        return self.score > 0

lst_in = ['Балакирев; 34; 2048',
'Mediel; 27; 0',
'Влад; 18; 9012',
'Nina P; 33; 0']

players = []
for i in lst_in:
    name = (i.split(';')[0])
    old = (i.split(';')[1].lstrip())
    score = int(i.split(';')[2].lstrip())
    players.append(Player(name, old, score))

players_filtered = list(filter(lambda x: x, players))
