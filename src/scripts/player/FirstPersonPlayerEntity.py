from ursina import *
from player.PlayerEntity import PlayerEntity


class FirstPersonPlayerEntity(PlayerEntity):
    def __init__(self, **kwargs):
        super().__init__(model='cube', color=color.orange, origin_y=-.5, **kwargs)
        self.camera_pivot = Entity(parent=self, y=1.5)
        camera.parent = self.camera_pivot
        camera.position = (0, 0, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 90
        mouse.locked = True

        # 视角切换标志
        self.first_person = True

        # 第三人称摄像机位置
        self.third_person_camera_pos = Vec3(0, 2, -5)
        self.third_person_camera_rot = Vec3(10, 0, 0)

    def update(self):
        super().update()
        self.camera_control()

    def camera_control(self):
        if self.first_person:
            self.rotation_y += mouse.velocity[0] * 40
            self.camera_pivot.rotation_x -= mouse.velocity[1] * 40
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)
            camera.position = self.third_person_camera_pos
            camera.rotation = self.third_person_camera_rot
        else:
            self.rotation_y += mouse.velocity[0] * 40
            self.camera_pivot.rotation_x -= mouse.velocity[1] * 40
            self.camera_pivot.rotation_x = clamp(self.camera_pivot.rotation_x, -90, 90)
            camera.position = self.third_person_camera_pos
            camera.rotation = self.third_person_camera_rot

    def input(self, key):
        if key == 'c':
            self.first_person = not self.first_person
            if self.first_person:
                camera.parent = self.camera_pivot
                camera.position = (0, 0, 0)
                camera.rotation = (0, 0, 0)
                mouse.locked = True
            else:
                camera.parent = self
                camera.position = self.third_person_camera_pos
                camera.rotation = self.third_person_camera_rot
                mouse.locked = True
