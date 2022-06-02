from graphics import*

class Wheel(object):
    def __init__(self,centre,wheel_radius,tire_radius):
        self.tire_circle=Circle(centre,tire_radius)
        self.wheel_circle=Circle(centre,wheel_radius)

    def draw(self,win):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move(self,dx,dy):
        self.tire_circle.move(dx,dy)
        self.wheel_circle.move(dx,dy)

    def set_color(self,wheel_color,tire_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def undraw(self):
        self.tire_circle.undraw()
        self.wheel.undraw()

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_centre(self):
        return self.tire_circle.getCentre()

    def animate(self,win,dx,dy,n):

        if n>0:
             self.move(dx,dy)
             win.after(100,self.animate,win,dx,dy,n-1)

win=GraphWin('Wheel',700,500)
w=Wheel(Point(100,100),50,70)
w.draw(win)
w.set_color('pink','purple')
w.animate(win,1,0,100)


win.mainloop()
