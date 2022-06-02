from graphics import *
from wheel import *


class Car:
    def __init__(self,wheel1_center,wheel1_radius,wheel2_center,wheel2_radius,body_height):
        tire1_radius=wheel1_radius/0.6
        tire2_radius=wheel2_radius/0.6
        self.wheel1=Wheel(wheel1_center,wheel1_radius,tire1_radius)
        self.wheel2=Wheel(wheel2_center,wheel2_radius,tire2_radius)
        self.rect=Rectangle(body_height)




win=GraphWin("Car",700,300)
# Create a car object
car= Car(Point(50, 50), 15, Point(100, 50), 15, 40)
car.draw(win)
# 1st wheel centred at 50, 50 with radius 15
wheel1=Wheel(Point(50,50),15,25)

# 2nd wheel centred at 100, 50 with radius 15
wheel2=Wheel(Point(100,50),15,25)

# Rectangle with a height of 40
rect=Rectangle(Point(10, 10), Point(200, 100))


car1 = Car(Point(50, 50), 15, Point(100, 50), 15, 40)
car1.draw(win)
# Color the wheels grey with black tires, and the body pink
car1.set_color('black', 'grey', 'pink')
# Make the car move on the screen
car1.animate(win, 1, 0, 400)
win.mainloop()

