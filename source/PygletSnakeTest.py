
import pyglet
from pyglet.window import key
from pyglet.window import mouse

from ObserverClasses import keySubject

from SnakeClass import Snake

from Wall import WallSegment


#resources_folder = "Resources\\"
resources_folder = "Resources/"

print("Booting...")
print("Root... ", __file__ )

#fps_display = pyglet.clock.ClockDisplay()
window = pyglet.window.Window()


mainsnake = Snake((200,200))
wall_list = list()
wall_list.append( WallSegment((50,50)) )
wall_list.append( WallSegment((50,100)) )
wall_list.append( WallSegment((50,150)) )
wall_list.append( WallSegment((50,200)) )



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
    mainsnake.snakehead.draw()
    for i in mainsnake.snakebody:
        i.draw().draw()
    for i in wall_list:
        i.draw().draw()


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