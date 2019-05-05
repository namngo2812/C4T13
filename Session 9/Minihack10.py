_highscores = ['45', '67', '56', '78']
def printHighScores():
    print('High scores!')
    for i, value in enumerate(_highscores, 1):
        print(i, value, sep = '.')
        
# print('High scores!')
# for i, value in enumerate(_highscores, 1):
#     print(i, value, sep = '.')
printHighScores()
click = input('Enter yout new score: ')
_highscores.append(click)
printHighScores()
# for i, value in enumerate(_highscores, 1):
#     print(i, value, sep = '.')

