from cmu_graphics import *

def onAppStart(app):
    app.paused = True

def redrawAll(app):
    drawLabel('112 Murder Mystery', 200, 200)

runApp()