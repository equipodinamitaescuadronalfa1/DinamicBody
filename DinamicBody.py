#!/usr/bin/env python3

'''
	DinamicBody.py Solve the n-body problem using Newton
	Copyright (C) 2019  equipodinamitaescuadronalfa1

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 




G=6.674e-11         #m^3kg^-1s^-2

class Particle:
    
    def __init__(self, p, v, m, dt=1):
        self.p = p
        self.v = v
        self.m = m
        self.dt = dt
        
    def setdt(self,dt):
        self.dt = dt
        

    def computeR(self,p1):
        r = math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2)
        return r

    def computeU(self,p1):
        u=[0,0,0]
        i=0
        for a,b in zip(self.p,p1):
            u[i] = b - a
            i+=1
        return u
    
    '''def integrate(self,dt,p1,m1):
        r = self.computeR(p1)
        u = self.computeU(p1)

        Vx=(G*m1*dt/(r**3))*u[0]
        Vy=(G*m1*dt/(r**3))*u[1]
        Vz=(G*m1*dt/(r**3))*u[2]
        
        
        self.v[0]+=Vxself.v[0]+Vx
        self.v[1]+=Vxself.v[0]+Vy
        self.v[2]+=Vxself.v[0]+Vz
        
        self.p = [self.p[0]+ (self.v[0]) *dt,self.p[1]+ (self.v[1])*dt,self.p[2]+ (self.v[2])*dt]'''
    def integrate(self,B):
        r = self.computeR(B.p)
        u = self.computeU(B.p)

        Vx=(G*B.m*self.dt/(r**3))*u[0]
        Vy=(G*B.m*self.dt/(r**3))*u[1]
        Vz=(G*B.m*self.dt/(r**3))*u[2]
        
        
        self.v[0]+=Vx
        self.v[1]+=Vy
        self.v[2]+=Vz
        
        self.p = [self.p[0]+ (self.v[0]) *dt,self.p[1]+ (self.v[1])*dt,self.p[2]+ (self.v[2])*dt]

    def getPosition(self):
        return self.p

    def getKineticEnergy(self):
        k= (1/2)*self.m*(math.sqrt( self.v[0]^2 +self.v[1]^2+self.v[2]^2))
        return k
    
    def getVelocity(self):
        return self.v


    
    
p0=[5e-2, 1e-3, 0.0]  #km
v0=[0.0, 0.0, 0.0]  #km/s
m=1e7         #kg

p1=[0.0, 0.0, 0.0]  #km
v1=[1.0, 0.0, 0.0]  #km/s
m1=1.0               #kg


dt=0.001              #sec

A = Particle(p0,v0,m)
B = Particle(p1,v1,m1)

B.setdt(dt)

x=[]
y=[]

v=[]

a=[]


x.append(0)
#y.append(B.getPosition()[0])
y.append(B.getPosition())
v.append(B.getVelocity()[0])
a.append(0.0)
v1=B.getVelocity()[0]


'''
for t in range(1,100):
    lastx=B.getPosition()[0]
    lastv=v1
    B.integrate(A)
    print(B.getPosition())
    
    x.append(float(t)*dt)
    y.append(B.getPosition()[0])
    v1=(B.getPosition()[0] - lastx) / B.dt
    
    v.append(v1)
    
    a.append((v1 - lastv) / B.dt)
    
'''

for t in range(1,100):
    B.integrate(A)
    x.append(float(t)*dt)
    y.append(B.getPosition())
    



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for point in y:
    ax.scatter(point[0],point[1],point[2],marker='o')
pointA=A.getPosition()
ax.scatter(pointA[0],pointA[1],pointA[2],marker='o')
plt.show()


'''
fig, ax = plt.subplots(3)
ax[0].plot(x,y)
ax[0].set(xlabel='time[Sec]',ylabel='position[KM]')
ax[0].grid()


ax[1].plot(x,v)
ax[1].set(xlabel='time[Sec]',ylabel='Velocity[KM]')
ax[1].grid()

ax[2].plot(x,a)
ax[2].set(xlabel='time[Sec]',ylabel='Acceleration[KM]')
ax[2].grid()

plt.show()
'''

