import pygame
import OpenGL.GL
import OpenGL.GLU

#### INITIALIZATION 
pygame.init()

gl_version = (3, 3)  # GL Version number (Major, Minor)
# By setting these attributes we can choose which Open GL Profile
# to use, profiles greater than 3.2 use the modern rendering path
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, gl_version[0])
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, gl_version[1])
pygame.display.gl_set_attribute(
    pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
)

#### setup viewport: specify that we'll be using OpenGL with double buffering
pygame.display.set_mode( (800,600), 
                        pygame.DOUBLEBUF|pygame.OPENGL, 
                        pygame.RESIZABLE)
#pygame.display.toggle_fullscreen()

while 1:
    #### handle user events
    for e in pygame.event.get():  
        #### handle quit event     
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):   
            pygame.quit()
            import sys; sys.exit()
    
    OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT|OpenGL.GL.GL_DEPTH_BUFFER_BIT)## wtf?
    pygame.display.flip()