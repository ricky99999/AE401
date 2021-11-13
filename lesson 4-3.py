from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
a = 0
while a<5:
    mc.setBlocks(x+10, y-30, z, x-10, y+1, z, 19)
    z = z-5
    a = a+1