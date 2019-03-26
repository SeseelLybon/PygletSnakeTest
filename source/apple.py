
from Collision import Collider
from Collision import collisionmanager
import pyglet

from random import randint

class Apple(Collider):

    resources_folder = "Resources/"
    apple_image = pyglet.resource.image(resources_folder+'apple.png')

    def __init__(self, pos):
        Collider.__init__(self)
        self.apple_sprite = pyglet.sprite.Sprite(self.apple_image, x=pos[0], y=pos[1] )

    def draw(self):
        return self.apple_sprite

    def position(self):
        return self.apple_sprite.x,self.apple_sprite.y

    def eat(self):
        self.apple_sprite.update(x=0,y=0)
        while True:
            x=(randint(1,11))*50
            y=(randint(1,8))*50
            print("Trying position", x, y)
            collisions = collisionmanager.check_collision(self, (x,y) )

            if not collisions:
                break

            print("Position blocked, trying again")
        self.apple_sprite.update(x=x,y=y)