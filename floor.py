
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y-1,z+1,x+2,y-1, z-1, 100)
mc.setBlock(x+1,y-1,z,11)