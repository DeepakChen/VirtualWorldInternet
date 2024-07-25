from ursina import *

class PlayerEntity(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 8
        self.collider = BoxCollider(self, Vec3(0,1,0), Vec3(1,2,1))

    def update(self):
        self.move()

    def move(self):
        if held_keys['w']:
            self.position += self.forward * self.speed * time.dt
        if held_keys['s']:
            self.position -= self.forward * self.speed * time.dt
        if held_keys['a']:
            self.position -= self.right * self.speed * time.dt
        if held_keys['d']:
            self.position += self.right * self.speed * time.dt

