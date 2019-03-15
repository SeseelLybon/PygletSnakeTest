
from Collision import Collider
import pyglet

class WallSegment(Collider):

    resources_folder = "Resources/"
    ball_image = pyglet.resource.image(resources_folder+'ball.png')

    def __init__(self, pos):
        Collider.__init__(self)
        self.wall_sprite = pyglet.sprite.Sprite(self.ball_image, x=pos[0], y=pos[1] )

    def draw(self):
        return self.wall_sprite

    def position(self):
        return self.wall_sprite.x,self.wall_sprite.y