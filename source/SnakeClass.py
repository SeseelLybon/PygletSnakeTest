

from pyglet.window import key
import pyglet

from ObserverClasses import KeyObserver
from Collision import Collider
from apple import Apple

class Snake(KeyObserver, Collider):

    movespeed = 50 # pixels
    resources_folder = "Resources/"
    ball_image = pyglet.resource.image(resources_folder+'ball.png')

    def __init__(self, startpos : tuple ):
        
        KeyObserver.__init__(self)
        Collider.__init__(self)
        self.snakehead = pyglet.sprite.Sprite(self.ball_image, x=startpos[0], y=startpos[1] )
        self.snakebody = []

        for dummy in range(0,3):
            self.appendSnakeSegment()

    def position(self):
        return self.snakehead.x ,self.snakehead.y

    def appendSnakeSegment(self):
        self.snakebody.append( SnakeSegement(
                                pyglet.sprite.Sprite(self.ball_image, x=self.snakehead.x, y=self.snakehead.y
                             )))

    def move_body(self, move : list ):
        prevpos = [ self.snakehead.x, self.snakehead.y ]
        self.snakehead.update(x=move[0]+self.snakehead.x,
                              y=move[1]+self.snakehead.y)
        #temppos = [ int(), int() ]
        for segment in self.snakebody:
            segment = segment.segment
            temppos = [ segment.x, segment.y ]
            segment.update( prevpos[0], prevpos[1])
            prevpos = temppos


    def on_key_press(self, observable, *args, **kwargs):

        move = [0, 0]
        symbol = args[0]
        modifier = args[1]
        self.movespeed = 50 # pixels
        if symbol == key.W:
            move[1] += self.movespeed

        elif symbol == key.S:
            move[1] -= self.movespeed

        elif symbol == key.A:
            move[0] -= self.movespeed

        elif symbol == key.D:
            move[0] += self.movespeed
        collisions = self.collisionmanager.check_collision(self, tuple(move))

        for i in collisions:
            if isinstance(i, Apple):
                i.eat()
                self.move_body(move)
                self.appendSnakeSegment()
        if not collisions:
            self.move_body(move)

    def draw(self):
        return [self.snakehead, self.snakebody ]


class SnakeSegement(Collider):

    def __init__(self, sprite):
        self.segment = sprite
        Collider.__init__(self)

    def draw(self):
        return self.segment

    def position(self):
        return self.segment.x ,self.segment.y

