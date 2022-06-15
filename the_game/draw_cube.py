import pygame
import OpenGL.GL

#cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
x = y = z = 50
cubeVertices = ((x,y,z),(x,y,-z),(x,-y,-z),(x,-y,z),(-x,y,z),(-x,-y,-z),(-x,-y,z),(-x,y,-z))

cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wireCube():
    #OpenGL.GL.glPushMatrix()
    OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            OpenGL.GL.glVertex3fv(cubeVertices[cubeVertex])
    OpenGL.GL.glEnd()
    #OpenGL.GL.glPopMatrix()
