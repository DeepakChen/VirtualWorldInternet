from ursina import *

class Camera(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fov = 90
        self.rotation_speed = 40

    def update(self):
        self.rotation_y += mouse.velocity[0] * self.rotation_speed
        self.rotation_x -= mouse.velocity[1] * self.rotation_speed
        self.rotation_x = clamp(self.rotation_x, -90, 90)
