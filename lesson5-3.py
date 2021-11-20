from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x, y, z = mc.player.getTilePos()
if mc.getBlock(x, y-1, z) == 12:
    target = random.choice(0, 81)
    mc setBlock(x, y, z, target)
    else:
        target = random.randint(1, 8)
        mc.setBlocks(x, y, z, x+5, y, z+5, 38, target)
    