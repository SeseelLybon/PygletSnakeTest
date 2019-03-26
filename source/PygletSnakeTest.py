
import pyglet
from pyglet.window import key
from pyglet.window import mouse

from ObserverClasses import keySubject

from random import randint

from SnakeClass import Snake
from apple import Apple
from wall import WallSegment


#resources_folder = "Resources\\"
resources_folder = "Resources/"

print("Booting...")
print("Root... ", __file__ )

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window()


mainsnake = Snake((200,200))
wall_list = list()
for i in range(0,13):
    i = i*50
    wall_list.append( WallSegment((i,0)) )
    wall_list.append( WallSegment((i,9*50)) )

for i in range(1,9):
    i = i*50
    wall_list.append( WallSegment((0,i)) )
    wall_list.append( WallSegment((12*50,i)) )

# Add randomly placed walls to make the game more difficult
# Field size is 11 by 8

for dummy in range(0, 8):

    x = (randint(1,11))*50
    y = (randint(1,8))*50

    wall_list.append( WallSegment((x,y)) )

apple = Apple((300,300))



label = pyglet.text.Label('Hello, world',
                        font_name='Times New Roman',
                        font_size=36,
                        x=window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    #sprites = list()
    window.clear()
    #fps_display.draw()
    apple.draw().draw()
    for i in mainsnake.snakebody:
        i.draw().draw()
    for i in wall_list:
        i.draw().draw()
    mainsnake.snakehead.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print("Hello world")
    keySubject.notify_observers(symbol, modifiers)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('Clicked at', x, y)


print("Pyglet.run()")
pyglet.app.run()

print("End of main")