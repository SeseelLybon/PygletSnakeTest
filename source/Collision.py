
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
        print(collisions)
        return collisions
                
collisionmanager = CollisionManager()
            
class Collider:
    collisionmanager = collisionmanager

    def __init__(self):
        collisionmanager.register_observer(self)

    def on_collision(self, *args, **kwargs):
        print('Got', args, kwargs, 'From', collisionmanager)

    def position(self):
        print("position not implemented at", self)


