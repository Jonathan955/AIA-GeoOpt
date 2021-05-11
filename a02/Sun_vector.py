# Assigment 02
# Jonathan Hernandez
# Sun vector

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math

#create a sun vector

#1. create a Sphere at point (0,0,0) with radius 1 and output it to a
#output the sphere to a

PtC = rg.Point3d(0,0,0)
a = rg.Sphere(PtC, 1)



#2. evaluate a point in the sphere using rg.Sphere.PointAt() at coordintes x and y
#the point should only be on the upper half of the sphere (upper hemisphere)
#the angles are in radians, so you might want to use math.pi for this
#output the point to b


b = rg.Sphere.PointAt(a,x,y)
#print b

#create a vector from the origin  and reverse the vector
#keep in mind that Reverse affects the original vector
#output the vector to c

c = rs.CreateVector(b)
c = rg.Vector3d.Negate(c)

