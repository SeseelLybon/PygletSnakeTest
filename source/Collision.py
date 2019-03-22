
class CollisionManager:
    def __init__(self):
        self._colliders = list()
    
    def register_observer(self, collider):
        self._colliders.append(collider)
    
    def check_collision(self, thing, offset=(0,0) ):
        collisions = list()
        for collider in self._colliders:
            if collider.position() == (thing.position()[0] + offset[0],
                                     thing.position()[1] + offset[1]):
                if collider != thing:
                    collisions.append(collider)
        if collisions:
            print(thing, "triggered collisions", "\n\t", collisions)
        return collisions

    def unregister_observer(self, observer):
        if observer in self._colliders:
            self._colliders.pop(collisionmanager._colliders.index(observer))
        pass

collisionmanager = CollisionManager()
            
class Collider:
    #collisionmanager = collisionmanager

    def __init__(self):
        collisionmanager.register_observer(self)

    def __del__(self):
        collisionmanager.unregister_observer(self)
        print("called collision destructor")

    def on_collision(self, *args, **kwargs):
        print('Got', args, kwargs, 'From', collisionmanager)

    def position(self):
        print("position not implemented at", self)


