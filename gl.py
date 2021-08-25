import pyglet
from pyglet.gl import *
from shaderpy import Shader

class FragmentView(pyglet.window.Window):
    def __init__(self):
        super(FragmentView, self).__init__(caption = 'FragmentView', width = 1024, height = 1024)
        self.shader = Shader([
        ('shader.v.glsl', GL_VERTEX_SHADER),
        ('sc.f.glsl', GL_FRAGMENT_SHADER)
        ])

        self.on_draw()

    def on_draw(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1., 1., 1., -1., 0., 1.)
    
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    
        self.shader.bind()

        glBegin(GL_QUADS)

        glVertex2i(-1, -1)
        glTexCoord2i(0, 0)
        
        glVertex2f(1, -1)
        glTexCoord2i(1, 0)

        glVertex2i(1, 1)
        glTexCoord2i(1, 1)

        glVertex2i(-1, 1)
        glTexCoord2i(0, 1)

        glEnd()
    
        self.shader.unbind()
    
window = FragmentView()
pyglet.app.run()