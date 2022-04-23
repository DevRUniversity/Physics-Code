from matplotlib import pyplot as plt
import math
Gravitational_constant = 0.00000000006674
bounds_of_calculation_left = -10000
bounds_of_calculation_right = 10000

class Gravitational_Object:
    x_cord = 0 #meters
    y_cord = 0 #meters
    x_velocity = 0
    y_velocity = 0
    mass = 1 #kg

    def __init__(self, x, y,v_x,v_y,inMass):
        self.x_cord = x
        self.y_cord = y
        self.x_velocity = v_x
        self.y_velocity = v_y
        self.mass = inMass

    def get_force_from_points(self, distance_x, distance_y,distance_z, mass_two):
        magnitude =( (abs(distance_x - x_cord) ** 2) + (abs(distance_y - y_cord) ** 2))**0.5
        return (Gravitational_constant*mass_two)/magnitude

    def accelerate_this_by(self,distance_x,distance_y,mass_two):
        magnitude = ((abs(distance_x - self.x_cord) ** 2) + (abs(distance_y - self.y_cord) ** 2)) ** 0.5
        acceleration = (Gravitational_constant*mass_two)/magnitude
        x_unit_component_of_velocity_times_acceleration = float(abs(distance_x - self.x_cord) )/ magnitude * acceleration
        y_unit_component_of_velocity_times_acceleration = float(abs(distance_y - self.y_cord) )/ magnitude * acceleration
        self.x_velocity = self.x_velocity + 10000000
        self.y_velocity = self.y_velocity + 10000000

ListOfGravitationalObjects = []
newX = []
newY = []
oldX = []
oldY = []

def animate(x_0, y_0, x_1, y_1):
    newX.append(x_1)
    newY.append(y_1)
    oldX.append(x_0)
    oldY.append(y_0)

    # Mention x and y limits to define their range
    plt.xlim(bounds_of_calculation_left, bounds_of_calculation_right)
    plt.ylim(bounds_of_calculation_left, bounds_of_calculation_right)

    # Ploting graph
    plt.scatter(newX, newY, color='blue')
    plt.scatter(oldX, oldY, color='white')
    plt.pause(0.001)

GravObj1 = Gravitational_Object(0,0,10,10,10000)
GravObj2 = Gravitational_Object(100,-200,10,10,1000)
ListOfGravitationalObjects.append(GravObj1)
ListOfGravitationalObjects.append(GravObj2)

counter = 0
while(counter < 10):
    PreviousGravObjs = ListOfGravitationalObjects.copy()
    for objN1 in ListOfGravitationalObjects:
        for objN2 in ListOfGravitationalObjects:
            if(objN1 != objN2):
                objN1.accelerate_this_by(distance_x = objN2.x_cord,distance_y = objN2.y_cord,mass_two = objN2.mass)
                print("acceleration!")
    for i in range(0,len(ListOfGravitationalObjects)):
        animate(PreviousGravObjs[i].x_cord,PreviousGravObjs[i].y_cord,
                ListOfGravitationalObjects[i].x_cord,ListOfGravitationalObjects[i].y_cord)

    counter = counter + 1

plt.show()