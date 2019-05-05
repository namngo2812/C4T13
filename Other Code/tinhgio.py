import datetime
import pyglet
hour = int(input("Nhap gio cua ban: "))

currentDT = datetime.datetime.now().hour
print(currentDT)
while True:
    if currentDT == hour:  

        music = pyglet.resource.media('sample.wav', streaming=False)
        music.play()
        print('chay nhac')
        pyglet.app.run()



