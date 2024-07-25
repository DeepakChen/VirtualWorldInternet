from ursina import *
from scripts.utils.Logger import Logger;
from world.WorldManager import WorldManager
from player.FirstPersonPlayerEntity import FirstPersonPlayerEntity

def main():
    logger = Logger().getLogger()
    logger.info("Virtual World Internet is being preloaded.")

    app = Ursina()
    logger.debug("Ursina App has been created.")

    # 初始化世界
    world_manager = WorldManager()
    logger.debug("WorldManager has been created.")
    world_manager.generate_world()
    logger.debug("World has been generated.")

    # 初始化玩家
    player = FirstPersonPlayerEntity()
    logger.debug("Player has been created.")

    # 设置摄像机
    def update():
        player.update()

    app.run()
    logger.info("Virtual World Internet has been loaded.")

if __name__ == '__main__':
    main()
