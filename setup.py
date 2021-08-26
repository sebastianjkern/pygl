from setuptools import setup

setup(
    name="pygl",
    version="0.0.2",
    description="Python wrapper code to run glsl shader in opengl window",
    url="git@github.com:sebastianjkern/pygl.git",
    author="sebastianjkern",
    license="MIT",
    packages=['pygl'],
    data_files=[('shaders', ["pygl/sc.f.glsl", "pygl/shader.v.glsl"])]
)