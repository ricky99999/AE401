# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:19:56 2021

@author: bella
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
time.sleep(5)
position=mc.player.getTilePos()
x=position.x
y=position.y
z=position.z
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
