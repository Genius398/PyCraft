from pyglet.window import key
from pyglet.gl import *
import math

class Player:
    def __init__(self, pos=(0, 0, 0), rot=(0, 0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.x = 0
        self.y = 0
        self.z = 0
        self.rotY = 0
        self.rotX = 0

    def mouse_motion(self, dx, dy):
        self.rot[0] += dy/8
        self.rot[1] -= dx/8
        if self.rot[0]>90:
            self.rot[0] = 90
        elif self.rot[0] < -90:
            self.rot[0] = -90

    def update(self,dt,keys):
        sens = 0.3
        s = dt*10
        rotY = -self.rot[1]/180*math.pi
        dx, dz = s*math.sin(rotY), math.cos(rotY)
        if keys[key.W]:
            self.pos[0] += dx*sens
            self.pos[2] -= dz*sens
        if keys[key.S]:
            self.pos[0] -= dx*sens
            self.pos[2] += dz*sens
        if keys[key.A]:
            self.pos[0] -= dz*sens
            self.pos[2] -= dx*sens
        if keys[key.D]:
            self.pos[0] += dz*sens
            self.pos[2] += dx*sens
        if keys[key.SPACE]:
            self.pos[1] += s
        if keys[key.LSHIFT]:
            self.pos[1] -= s

        self.x = self.pos[0]
        self.y = self.pos[2]
        self.z = self.pos[1]

        self.rotY = self.rot[0]
        self.rotX = self.rot[1]
