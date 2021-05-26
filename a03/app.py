from flask import Flask
import ghhops_server as hs
import rhino3dm
import numpy as np



# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/pointat",
    name="PointAt",
    description="Get point along curve",
    icon="pointat.png",
    inputs=[
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameter on Curve to evaluate"),
    ],
    outputs=[
        hs.HopsPoint("P", "P", "Point on curve at t")
    ]
)
def pointat(curve, t):
    pt = curve.PointAt(t)
    n = np.array([pt.X, pt.Y, pt.Z])
    n2 = np.array([1,2,3])
    n3 = n + n2
    print(type(n))
    
    
    return rhino3dm.Point3d(n3[0], n3[1], n3[2])

if __name__ == "__main__":
    app.run()