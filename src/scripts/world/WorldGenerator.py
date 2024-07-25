from ursina import *

class WorldGenerator:
    def __init__(self):
        pass

    def generate_terrain(self):
        ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))

        # 示例：生成一些随机的立方体作为互联网节点
        for i in range(16):
            Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1,2),
                   x=random.uniform(-8,8), z=random.uniform(-8,8) + 8, collider='box',
                   scale_y=random.uniform(2,3), color=color.hsv(0, 0, random.uniform(.9, 1)))

        # 添加一些平台
        for i in range(10):
            Entity(model='cube', origin_y=-.5, scale=(3, 1, 3), texture='brick', texture_scale=(1,2),
                   x=random.uniform(-8,8), y=2, z=random.uniform(-8,8), collider='box', color=color.hsv(0, 0, random.uniform(.9, 1)))
