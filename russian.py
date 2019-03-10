# while True:
#     a = input("Your number: ")
#     print("Your number you entered has: ",len(a)," digits ") 
#     break

import pyglet

music = pyglet.resource.media('sample.mp3')
music.play()


pyglet.app.run()



