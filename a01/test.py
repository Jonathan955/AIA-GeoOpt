import Rhino.Geometry as rg

grid = []
for i in range(10):
    for j in range(10):
        grid.append( rg.Point3d(i,j,0) )

a = grid