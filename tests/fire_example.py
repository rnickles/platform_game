import pygame
import OpenGL.GL
import OpenGL.GLU
fire = [
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0xc0, 0x00, 0x00, 0x01, 0xf0,
0x00, 0x00, 0x07, 0xf0, 0x0f, 0x00, 0x1f, 0xe0,
0x1f, 0x80, 0x1f, 0xc0, 0x0f, 0xc0, 0x3f, 0x80,
0x07, 0xe0, 0x7e, 0x00, 0x03, 0xf0, 0xff, 0x80,
0x03, 0xf5, 0xff, 0xe0, 0x07, 0xfd, 0xff, 0xf8,
0x1f, 0xfc, 0xff, 0xe8, 0xff, 0xe3, 0xbf, 0x70,
0xde, 0x80, 0xb7, 0x00, 0x71, 0x10, 0x4a, 0x80,
0x03, 0x10, 0x4e, 0x40, 0x02, 0x88, 0x8c, 0x20,
0x05, 0x05, 0x04, 0x40, 0x02, 0x82, 0x14, 0x40,
0x02, 0x40, 0x10, 0x80, 0x02, 0x64, 0x1a, 0x80,
0x00, 0x92, 0x29, 0x00, 0x00, 0xb0, 0x48, 0x00,
0x00, 0xc8, 0x90, 0x00, 0x00, 0x85, 0x10, 0x00,
0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00
]

#### INITIALIZATION 
pygame.init()
#### setup viewport: specify that we'll be using OpenGL with double buffering
pygame.display.set_mode( (400,400), 
                        pygame.DOUBLEBUF|pygame.OPENGL, 
                        pygame.RESIZABLE)
pygame.display.toggle_fullscreen()

#OpenGL.GLU.gluPerspective(45, 1, 0.1, 1)
OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT|OpenGL.GL.GL_DEPTH_BUFFER_BIT)## wtf?
OpenGL.GL.glColor3f(1.0,0,0)

import os
resource_path = os.path.join(os.getcwd(), "the_game", "resources", "i_bar_icon.bmp")
resource_surface = pygame.image.load_basic( resource_path )
resource_bitmap = pygame.image.tostring( resource_surface, "RGBX", True)
#print(string(resource_bitmap))
#OpenGL.GL.glWindowPos2i(0, 0)
OpenGL.GL.glRasterPos2i(0, 0)
OpenGL.GL.glBitmap(64,64, 0,0,0,0, resource_bitmap)
#OpenGL.GL.glBitmap(32,32, 0,0,32,0, fire)

pygame.display.flip()

while 1:
    #### handle user events
    for e in pygame.event.get():       
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):   
            pygame.quit()
            import sys; sys.exit()
