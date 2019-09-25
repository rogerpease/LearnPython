#!/usr/bin/python3.5
#import sys
#import time


#import mcpi.minecraft as minecraft; 
#mc=minecraft.Minecraft.create()

maze = [[ 1,0,1,1,1], 
        [ 1,0,1,0,1], 
        [ 1,0,1,0,1], 
        [ 1,0,0,0,1], 
        [ 1,1,1,0,1], 
        [ 1,0,0,0,1], 
        [ 1,0,1,1,1], 
        [ 1,0,1,0,1]]

#
# Draw the maze. 
#
for x in range(len(maze)):
  for y in range (len(maze[x])):
    print (maze[x][y], end='')
  print ()

# NETHER_REACTOR_CORE = 247
#while True: 
#     blockid = input("Block to add")
#     x,y,z = mc.player.getPos()
#     mc.setBlock(x,y,z,int(blockid),1)

#     mc.player.setPos() 

