

from pyglet.window import key
import pyglet

from ObserverClasses import KeyObserver
from ObserverClasses import keySubject


class Snake(KeyObserver):
    
    resources_folder = "Resources/"
    movespeed = 50 # pixels
    ball_image = pyglet.resource.image(resources_folder+'ball.png')

    def __init__(self, startpos : tuple ):
        
        super().__init__(keySubject)
        self.snakehead = pyglet.sprite.Sprite(self.ball_image, x=startpos[0], y=startpos[1] )
        self.snakebody = []
        self.appendSnakeSegment()
        self.appendSnakeSegment()
        self.appendSnakeSegment()
        self.appendSnakeSegment()

    def appendSnakeSegment(self):
        if len(self.snakebody) == 0:
            self.snakebody.append(pyglet.sprite.Sprite(self.ball_image,
                                                       x=self.snakehead.x,
                                                       y=self.snakehead.y ))
        else:
            self.snakebody.append(pyglet.sprite.Sprite(self.ball_image,
                                                       x=self.snakebody[-1].x,
                                                       y=self.snakebody[-1].y ))

    def move_body(self, move : list ):
        prevpos = [ self.snakehead.x, self.snakehead.y ];
        self.snakehead.update(x=move[0]+self.snakehead.x,
                              y=move[1]+self.snakehead.y)
        temppos = [ int(), int() ];
        for segment in self.snakebody:
            temppos = [ segment.x, segment.y ]
            segment.x, segment.y = prevpos[0], prevpos[1]
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

        self.move_body(move)

    def draw():
        return [self.snakehead, self.snakebody]

class SnakeSegement():
    def __init__():
        pass


