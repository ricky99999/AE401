from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()
x, y, z = mc.player.getTilePos()

while True:
    steps = random.randint(1, 8)
    x = x + steps
    mc.player.setTilePos(x, y, z)
    time.sleep(3)
