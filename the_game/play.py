import pygame
import OpenGL.GL
import OpenGL.GLU
import entity
import mouse_events

def main(level):
    #### INITIALIZATION 
    pygame.init()
    #### setup viewport: specify that we'll be using OpenGL with double buffering
    pygame.display.set_mode( (100,100), 
                            pygame.DOUBLEBUF|pygame.OPENGL, 
                            pygame.RESIZABLE)
    pygame.display.toggle_fullscreen()
    pygame.display.set_caption("IBAR")
    #### build OpenGL frustrum
    s_x, s_y = pygame.display.get_window_size() 
    OpenGL.GLU.gluPerspective(45, (1.0*s_x/s_y), 100, 1000.0) #(GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar)
    OpenGL.GL.glTranslatef(-0.5*s_x, -0.5*s_y, -1000.0)
    #### display some instructions for the user
    rules = """Mouse wheel for zoom. Click and drag to move. Hold "d" and click and drag to draw a new platform. Press "Esc" to quit."""
    level.game_objects.add( entity.Rule_Display(rules) )
    #### setup clock
    FPS = 60
    clock = pygame.time.Clock()
    #### GAMELOOP
    time_since_last_ball = 50
    while 1:
        #### handle user events
        for e in pygame.event.get():       
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):   
                pygame.quit()
                import sys; sys.exit()
            mouse_events.mouseMove(e, level)
            ### pause menu 
            if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):   
                            pygame.quit()
                            import sys; sys.exit()
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False
                            break
                        mouse_events.mouseMove(e, level)
        #### drop ballz
        if time_since_last_ball <= 0:
            level.game_objects.add( entity.Ball((300,700), level.space) )
            time_since_last_ball = 50
        time_since_last_ball -= 1
        #### move the physics simulation forward one timestep
        # Prevent tunneling: Use a smaller value for dt in the call to space.step. 
        # A simple way is to call space.step multiple times each frame in your application. 
        # This will also help to make the overall simulation more stable.
        #level.space.step(1.0/FPS)
        level.space.step(1.0/(3.0*FPS))
        level.space.step(1.0/(3.0*FPS))
        level.space.step(1.0/(3.0*FPS))
        #### clear and render
        OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT|OpenGL.GL.GL_DEPTH_BUFFER_BIT)## wtf?
        for spr in level.game_objects:
            spr.render(level)
        pygame.display.flip()
        clock.tick(60)
#### RUN LEVEL
import level
main( level )