import pygame
import OpenGL.GL
import entity
#### ZOOM HELPER
def centered_zoom(center, scale_factor, level):
    x, y = level.screen_to_world( center )
    OpenGL.GL.glTranslatef(x, y, 0.0)
    OpenGL.GL.glScaled(scale_factor, scale_factor, scale_factor)
    OpenGL.GL.glTranslatef(-x, -y, 0.0)
#### HANDLE VARIOUS MOUSE EVENTS
mouse_drag_last_pos = False
mouse_start = False
def mouseMove(event, level):
    global mouse_drag_last_pos, mouse_start
    pressed = pygame.key.get_pressed()
    #### MOUSE-CENTERED ZOOM
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled forward
        centered_zoom(event.pos, 1.05, level)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled back
        centered_zoom(event.pos, 0.95, level)
    #### DRAG AND TRANSLATE (mouse press and move with no keys held down)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not pressed[pygame.K_d]:
        mouse_drag_last_pos = event.pos
    elif event.type == pygame.MOUSEMOTION and mouse_drag_last_pos:
        a, b = level.screen_to_world(mouse_drag_last_pos)
        c, d = level.screen_to_world(event.pos)
        dx, dy = c-a, d-b
        OpenGL.GL.glTranslatef(dx, dy, 0.0)
        mouse_drag_last_pos = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not pressed[pygame.K_d]:
        mouse_drag_last_pos = False
    #### STRAIGHT-LINE DRAWING (when the user holds the "D" key, draw a line between mouse_down and mouse_up)
    elif pressed[pygame.K_d] and event.type == pygame.MOUSEBUTTONDOWN:
        mouse_start = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and mouse_start:
        level.game_objects.add(entity.Platform( level.screen_to_world(mouse_start), 
                                                    level.screen_to_world(event.pos), 
                                                    level.space ) )
        mouse_start = False