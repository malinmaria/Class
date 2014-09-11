
#This program creates a Tic-Tac-Toe grid where the user can click in any square
#9 times to get alternating X's and O's


from graphics import *

win = GraphWin("Tic-Tac-Toe", 300,300)

pt1 = Point(100,0)
pt2 = Point(100,300)

line1 = Line(pt1,pt2)
line1.draw(win)

pt3 = Point(200,0)
pt4 = Point(200,300)

line2 = Line(pt3,pt4)
line2.draw(win)

pt5 = Point(0,200)
pt6 = Point(300,200)

line3 = Line(pt5,pt6)
line3.draw(win)

pt7 = Point(0,100)
pt8 = Point(300,100)

line4 = Line(pt7,pt8)
line4.draw(win)

numClicks = 9
#mouseClick = win.getMouse()

def drawX(centerX, centerY):
    centerPoint = Point(centerX, centerY)

    lineA = Line(centerPoint, Point(centerX+40, centerY+40))
    lineA.draw(win)

    lineB = Line(centerPoint, Point(centerX+40, centerY-40))
    lineB.draw(win)

    lineC = Line(centerPoint, Point(centerX-40, centerY+40))
    lineC.draw(win)

    lineD = Line(centerPoint, Point(centerX-40, centerY-40))
    lineD.draw(win)

#User clicks, get mouse click point
#Find center of the click
#Alternate between drawing O and X
xClick = win.getMouse()
xPoint = findCenter(xClick)
drawX(xPoint.getX(),xPoint.getY())

oClick = win.getMouse()
cPoint = findCenter(oClick)
circle = Circle(cPoint,40)
circle.draw(win)

xClick = win.getMouse()
xPoint = findCenter(xClick)
drawX(xPoint.getX(),xPoint.getY())

oClick = win.getMouse()
cPoint = findCenter(oClick)
circle = Circle(cPoint,40)
circle.draw(win)

xClick = win.getMouse()
xPoint = findCenter(xClick)
drawX(xPoint.getX(),xPoint.getY())

oClick = win.getMouse()
cPoint = findCenter(oClick)
circle = Circle(cPoint,40)
circle.draw(win)

xClick = win.getMouse()
xPoint = findCenter(xClick)
drawX(xPoint.getX(),xPoint.getY())

oClick = win.getMouse()
cPoint = findCenter(oClick)
circle = Circle(cPoint,40)
circle.draw(win)

xClick = win.getMouse()
xPoint = findCenter(xClick)
drawX(xPoint.getX(),xPoint.getY())

def findCenter(point):
    x=point.getX()
    y=point.getY()
    newx=x//100*100+50
    newy=y//100*100+50
    #print(newx,newy)
    return Point(newx,newy)


