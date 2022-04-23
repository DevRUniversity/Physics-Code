from matplotlib import pyplot as plt
import math
import time
seconds_of_computation_time = 30
Gravitational_constant = 0.00000000006674
bounds_of_calculation_left = -10000
bounds_of_calculation_right = 10000
ListOfGravitationalObjects = []
newX = []
newY = []
oldX = []
oldY = []

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
        self.x_velocity = self.x_velocity + x_unit_component_of_velocity_times_acceleration
        self.y_velocity = self.y_velocity + y_unit_component_of_velocity_times_acceleration

    def update_positon(self):
        self.x_cord = self.x_cord + self.x_velocity
        self.y_cord = self.y_cord + self.y_velocity

def current_milli_time():
    return round(time.time() * 1000)

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
    #plt.scatter(oldX, oldY, color='white')
    plt.pause(0.0001)

GravObj1 = Gravitational_Object(0,0,10,10,10000)
GravObj2 = Gravitational_Object(100,-200,10,10,1000)
ListOfGravitationalObjects.append(GravObj1)
ListOfGravitationalObjects.append(GravObj2)

elapsed_milliseconds = 0
initial_milliseconds = current_milli_time()
counter = 0
while(elapsed_milliseconds / 1000 < seconds_of_computation_time):
    PreviousGravObjs = ListOfGravitationalObjects.copy()
    for objN1 in ListOfGravitationalObjects:
        for objN2 in ListOfGravitationalObjects:
            if(objN1 != objN2):
                objN1.accelerate_this_by(distance_x = objN2.x_cord,distance_y = objN2.y_cord,mass_two = objN2.mass)
    for i in range(0,len(ListOfGravitationalObjects)):
        ListOfGravitationalObjects[i].update_positon() #called here to avoid strange issues with the order in which calculations are made
        animate(PreviousGravObjs[i].x_cord,PreviousGravObjs[i].y_cord,
                ListOfGravitationalObjects[i].x_cord,ListOfGravitationalObjects[i].y_cord)
        
    elapsed_milliseconds = current_milli_time() - initial_milliseconds
    print(str(elapsed_milliseconds / 1000) + "of Computer Time Used")
plt.show()