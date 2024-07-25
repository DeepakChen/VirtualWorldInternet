from ursina import *
from world.WorldGenerator import WorldGenerator

class WorldManager(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generator = WorldGenerator()

    def generate_world(self):
        self.generator.generate_terrain()
