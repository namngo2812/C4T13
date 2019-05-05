games = ['gta', 'csgo', 'zelda']
print(games)
new_game = input("Game moi: ")
games.append(new_game)
print(*games, sep = '|')