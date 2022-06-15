import pygame       
import pymunk
import OpenGL.GLU
import OpenGL.GL
#### SETUP THE PHYSICS
space = pymunk.Space()     # Create a Space which contain the simulation
space.gravity = 0, -2000     # Set its gravity
#### SETUP THE GAME OBJECTS
game_objects = pygame.sprite.Group() ## Use a pygame group for added functionality 
#### SCREEN-TO-WORLD COORDINATE CONVERSION SYSTEM
def screen_to_world( pos ):
    x, y = pos
    viewport = OpenGL.GL.glGetIntegerv( OpenGL.GL.GL_VIEWPORT)
    y_max = viewport[3] 
    u_x, u_y, u_z = OpenGL.GLU.gluUnProject( x, y_max-y, 1, 
                                            OpenGL.GL.glGetDoublev( OpenGL.GL.GL_MODELVIEW_MATRIX), 
                                            OpenGL.GL.glGetDoublev( OpenGL.GL.GL_PROJECTION_MATRIX), 
                                            viewport )
    return u_x, u_y
def world_to_screen( pos ):
    x, y = pos
    viewport = OpenGL.GL.glGetIntegerv( OpenGL.GL.GL_VIEWPORT)
    y_max = viewport[3] 
    p_x, p_y, p_z = OpenGL.GLU.gluProject( x, y, 1,
                                            OpenGL.GL.glGetDoublev( OpenGL.GL.GL_MODELVIEW_MATRIX), 
                                            OpenGL.GL.glGetDoublev( OpenGL.GL.GL_PROJECTION_MATRIX), 
                                            viewport )
    return p_x, y_max - p_y 
