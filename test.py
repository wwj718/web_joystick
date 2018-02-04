#!/usr/bin/env python
# encoding: utf-8
import pygame
pygame.init()
while True:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    #print("I'm a main loop")
    joystick = pygame.joystick.Joystick(0)#只有一个
    joystick.init()
    name = joystick.get_name()
    # print("Joystick name: {}".format(name) )
    axes = joystick.get_numaxes()
    for i in range( axes ):
    # pygame.joystick.Joystick.get_axis
    # 选择你关心的axes选为元组 (0,1)
      axis = joystick.get_axis( i )
      print("Axis {} value: {:>6.3f}".format(i, axis) )

