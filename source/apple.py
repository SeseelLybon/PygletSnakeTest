
from Collision import Collider
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
        while True:
            x=(randint(100,600)//50)*50
            y=(randint(100,500)//50)*50
            collisions = self.collisionmanager.check_collision(self, (x,y) )
            if not collisions:
                break

            print("Position blocked, trying again")
        self.apple_sprite.update(x=x,y=y)