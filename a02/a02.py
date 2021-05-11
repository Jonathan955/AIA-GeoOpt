# Assigment 02
# Jonathan Hernandez

"""Provides a scripting component.
    Inputs:
        m: a mesh
        s: sun vector
    Output:
        a: List of Vectors
        b: List of Points
        c: list of angles
        d: exploded mesh
        """
        
import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th
import math
import ghpythonlib.components as ghc

#
#1.
#compute face normals using rg.Mesh.FaceNormals.ComputeFaceNormals()
#output the vectors to a
#

m.FaceNormals.ComputeFaceNormals
a = m.FaceNormals
#print(a)

#
#2.
#get the centers of each faces using rg.Mesh.Faces.GetFaceCenter()
#store the centers into a list called centers 
#output that list to b
#

centers = []
for i in range(m.Faces.Count):
    cen = m.Faces.GetFaceCenter(i)
    centers.append(cen)
    b = centers
#print(b)

#
#3.
#calculate the angle between the sun and each FaceNormal using rg.Vector3d.VectorAngle()
#store the angles in a list called angleList and output it to c
#

angleList = []
for i in a:
    ang = rg.Vector3d.VectorAngle(s,i)
    angleList.append(ang)
    
c = angleList
#print(c)

#
#4. explode the mesh - convert each face of the mesh into a mesh
#for this, you have to first copy the mesh using rg.Mesh.Duplicate()
#then iterate through each face of the copy, extract it using rg.Mesh.ExtractFaces
#and store the result into a list called exploded in output d
#

md = rg.Mesh.Duplicate(m)
mdf = md.Faces.Count
exploded = []
for i in range(mdf):
    emf = md.Faces.ExtractFaces([0])
    exploded.append(emf)
d = exploded
#print(d)
