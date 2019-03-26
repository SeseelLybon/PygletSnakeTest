

from pyglet.window import key
import pyglet

from ObserverClasses import KeyObserver
from Collision import Collider
from Collision import collisionmanager
from apple import Apple

class Snake(KeyObserver, Collider):

    movespeed = 50 # pixels
    resources_folder = "Resources/"

    snakehead_left_image = pyglet.resource.image(resources_folder+'snakehead_left.png')
    snakehead_right_image = pyglet.resource.image(resources_folder+'snakehead_right.png')
    snakehead_up_image = pyglet.resource.image(resources_folder+'snakehead_up.png')
    snakehead_down_image = pyglet.resource.image(resources_folder+'snakehead_down.png')

    snakebody_blanco_image = pyglet.resource.image(resources_folder+'snakebody_blanco.png')
    snakebody_lr_image = pyglet.resource.image(resources_folder+'snakebody_rl.png')
    snakebody_ud_image = pyglet.resource.image(resources_folder+'snakebody_ud.png')
    snakebody_ld_image = pyglet.resource.image(resources_folder+'snakebody_ld.png')
    snakebody_rd_image = pyglet.resource.image(resources_folder+'snakebody_rd.png')
    snakebody_lu_image = pyglet.resource.image(resources_folder+'snakebody_lu.png')
    snakebody_ru_image = pyglet.resource.image(resources_folder+'snakebody_ru.png')

    def __init__(self, startpos : tuple ):
        
        KeyObserver.__init__(self)
        Collider.__init__(self)
        self.snakehead = pyglet.sprite.Sprite(self.snakehead_left_image, x=startpos[0], y=startpos[1] )
        self.snakebody = []

        for dummy in range(0,3):
            self.appendSnakeSegment()

    def position(self):
        return self.snakehead.x ,self.snakehead.y

    def appendSnakeSegment(self):
        self.snakebody.append( SnakeSegement(
                                pyglet.sprite.Sprite(self.snakebody_blanco_image, x=self.snakehead.x, y=self.snakehead.y),
                                len(self.snakebody)
                             ))

    prevmovebody = [0, 0]

    def move_body(self, move : list ):
        prevpos = [ self.snakehead.x, self.snakehead.y ]
        self.snakehead.update(x=move[0]+self.snakehead.x,
                              y=move[1]+self.snakehead.y)

        if move[0] > 0:
            self.snakehead.image = self.snakehead_right_image
        elif move[0] < 0:
            self.snakehead.image = self.snakehead_left_image
        elif move[1] > 0:
            self.snakehead.image = self.snakehead_up_image
        elif move[1] < 0:
            self.snakehead.image = self.snakehead_down_image


        previmage=None
        doonce = True
        #temppos = [ int(), int() ]
        for segment in self.snakebody:
            segment = segment.segment
            temppos = [ segment.x, segment.y ]
            tempimage = segment.image
            segment.update( prevpos[0], prevpos[1])

            if doonce:
                if move[0] > 0:
                    if self.prevmovebody[1] > 0:
                        segment.image = self.snakebody_ld_image
                    elif self.prevmovebody[1] < 0:
                        segment.image = self.snakebody_lu_image
                    else:
                        segment.image = self.snakebody_lr_image
                elif move[0] < 0:
                    if self.prevmovebody[1] > 0:
                        segment.image = self.snakebody_rd_image
                    elif self.prevmovebody[1] < 0:
                        segment.image = self.snakebody_ru_image
                    else:
                        segment.image = self.snakebody_lr_image
                if move[1] > 0:
                    if self.prevmovebody[0] > 0:
                        segment.image = self.snakebody_ru_image
                    elif self.prevmovebody[0] < 0:
                        segment.image = self.snakebody_lu_image
                    else:
                        segment.image = self.snakebody_ud_image
                elif move[1] < 0:
                    if self.prevmovebody[0] > 0:
                        segment.image = self.snakebody_rd_image
                    elif self.prevmovebody[0] < 0:
                        segment.image = self.snakebody_ld_image
                    else:
                        segment.image = self.snakebody_ud_image

                doonce = False
            else:
                segment.image = previmage

            self.prevmovebody = move

            prevpos = temppos
            previmage = tempimage


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

        collisions = collisionmanager.check_collision(self, tuple(move))

        for i in collisions:
            if isinstance(i, Apple):
                self.move_body(move)
                i.eat()
                self.appendSnakeSegment()
            elif isinstance(i, SnakeSegement):
                temp = self.snakebody
                print([x.ID for x in self.snakebody])
                for seg in temp[:]:
                    if seg.ID > i.ID:
                        print("Deleting segment", seg.ID, "hit by", i.ID)
                        pos = self.snakebody.index(seg)
                        self.snakebody[pos].__del__()
                        self.snakebody.pop(pos)


                self.move_body(move)

        if not collisions:
            self.move_body(move)

    def draw(self):
        return [self.snakehead, self.snakebody ]

    def bite_self(self):
        pass

class SnakeSegement(Collider):

    num_segments = [0]

    def __init__(self, sprite, ssid):
        self.segment = sprite
        self.ID = ssid
        print("Created snakesegment with id", self.ID)
        Collider.__init__(self)

    def __del__(self):
        print("SnakeSegment del called")
        collisionmanager.unregister_observer(self)

    def draw(self):
        return self.segment

    def position(self):
        return self.segment.x ,self.segment.y

