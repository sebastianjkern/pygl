import pyglet
from pyglet.gl import *
from shaderpy import Shader

class FragmentView(pyglet.window.Window):
    def __init__(self, caption='FragmentView', width=500, height=500, vertex_shader_name="shader.v.glsl", fragment_shader_name="sc.f.glsl"):
        super(FragmentView, self).__init__(caption = caption, width = width, height = height)
        self.shader = Shader([
            (vertex_shader_name, GL_VERTEX_SHADER),
            (fragment_shader_name, GL_FRAGMENT_SHADER)
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

    def run(_):
        pyglet.app.run()

if __name__ == '__main__':
    window = FragmentView()
    window.run()