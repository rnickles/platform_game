import pygame
import pymunk
import OpenGL.GL
import math
#### BASE GAME OBJECT
class Entity(pygame.sprite.Sprite):         
    def __init__(self, *groups):
        super().__init__(*groups)
#### RULE DISPLAY OBJECT
class Rule_Display( Entity ):
    def __init__(self, text_string, *groups):
        super().__init__(*groups)
        font = pygame.font.SysFont("Sans", 24)
        self.text_surface = font.render(text_string, True, (0,255,255,100), (0,0,0,255)) 
        #pygame.image.save( self.text_surface, "rules.bmp" )    
        self.text_data = pygame.image.tostring(self.text_surface, "RGBA", True) 
    def render(self, level): 
        # bitmap = pygame.image.tostring(pygame.image.load_basic( "rules.bmp" ), "RGBA", True)    
        # OpenGL.GL.glBitmap( self.text_surface.get_width(), self.text_surface.get_height(),
        #                         300, 300, 100, 100, bitmap)
        OpenGL.GL.glDrawPixels(self.text_surface.get_width(), self.text_surface.get_height(), 
                                OpenGL.GL.GL_RGBA, 
                                OpenGL.GL.GL_UNSIGNED_BYTE, 
                                self.text_data)
#### PLATFORM OBJECT
class Platform(Entity): 
    def __init__(self, start, end, space, *groups):
        super().__init__(*groups)
        #### VARIABLES FOR OPENGL RENDERING
        self.vertices = (start, end)
        self.edges = [ (0,1) ]
        #### DEFINE THE PHYSICAL PROPERTIES
        self.body = pymunk.Segment(space.static_body, start, end, 10)
        self.body.elasticity = 2#0.95
        space.add(self.body) 
    #### OPENGL RENDERING METHOD    
    def render( self, level ):                         
        OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
        OpenGL.GL.glColor3f(0,1,1)
        for edge in self.edges:
            for vertex in edge:
                OpenGL.GL.glVertex2fv(self.vertices[vertex])
        OpenGL.GL.glEnd()
#### BALL OBJECT
class Ball(Entity): 
    def __init__(self, pos, space, *groups):
        super().__init__(*groups)
        #### DEFINE THE PHYSICAL PROPERTIES
        self.space = space
        self.body = pymunk.Body(1,1666)  # Create a Body with mass and moment
        self.body.position = pos      # Set the position of the body
        self.shape = pymunk.Circle(self.body, 8, (0, 0))
        self.shape.elasticity = 0.95
        self.shape.friction = 0.9
        self.space.add(self.body, self.shape)
    #### OPENGL RENDERING METHOD (doubling as an update method)
    def render(self, level):
        #### limit velocity to prevent tunnelling
        MAX_VELOCITY = -5000 # negative velocity due to gravity
        if self.body.velocity.y < MAX_VELOCITY:
             self.body.velocity = pymunk.Vec2d(self.body.velocity.x, MAX_VELOCITY)
        #### only render if the body isn't "too" far down
        x, y = self.body.position
        p_y =  level.world_to_screen( (x, y) )[0]
        y_max = OpenGL.GL.glGetIntegerv( OpenGL.GL.GL_VIEWPORT)[3]
        if p_y <= y_max+1000:
            OpenGL.GL.glBegin(OpenGL.GL.GL_POLYGON)
            OpenGL.GL.glColor3f(0,0.4,0)
            sides = 32    
            radius = 10
            for i in range(100):    
                cosine= radius * math.cos(i*2*math.pi/sides) + x    
                sine  = radius * math.sin(i*2*math.pi/sides) + y    
                OpenGL.GL.glVertex2f(cosine,sine)
            OpenGL.GL.glEnd()
        #### otherwise, the object is too far away and so free up those resources
        else: 
            self.space.remove( self.body, self.shape )
            level.game_objects.remove( self )
            

