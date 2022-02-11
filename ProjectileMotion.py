import sympy
import numpy
import matplotlib.pyplot as p1
import matplotlib.markers as MARKERS
import math

#global variables - beginning
time = 0
time_interval = 0.1
time_limit = 1000
#global variables - end


class Vector:
    x_direction = 0  # meters
    y_direction = 0  # meters
    z_direction = 0  # meters


def displacement_kinematic_equation(position,initial_velocity,acceleration,time):
    return position + (initial_velocity * time) + (acceleration * ((time) ** 2) * 0.5)

def change_vector_values(vector, x,y,z):
    vector.x_direction = x
    vector.y_direction = y
    vector.z_direction = z

def velocity_vector_from_angle_magnitude(angle,magnitude,VelocityVector):
    angle = math.radians(angle)
    change_vector_values(VelocityVector, magnitude*math.cos(angle), 0, magnitude*math.sin(angle))

def position_vector_invalid(PositionVector):
    if(PositionVector.z_direction > 0):
        return True
    if(PositionVector.z_direction <= 0):
        return False;


StartPositionVector = Vector();
VelocityVector = Vector();
PositionVector = Vector();
AccelerationVector = Vector();

change_vector_values(StartPositionVector,0,0,100)
change_vector_values(PositionVector,StartPositionVector.x_direction,StartPositionVector.y_direction,StartPositionVector.z_direction)
velocity_vector_from_angle_magnitude(90, 1000,VelocityVector)
change_vector_values(AccelerationVector,0,0,-9.80665)

xResult = []
yResult = []
zResult = []
check_criteria_met = True

while(time < time_limit and check_criteria_met):
    change_vector_values(PositionVector,
                         displacement_kinematic_equation(position=StartPositionVector.x_direction,initial_velocity=VelocityVector.x_direction,acceleration=AccelerationVector.x_direction, time=time),
                         displacement_kinematic_equation(position=StartPositionVector.y_direction,initial_velocity=VelocityVector.y_direction,acceleration=AccelerationVector.y_direction, time=time),
                         displacement_kinematic_equation(position=StartPositionVector.z_direction,initial_velocity=VelocityVector.z_direction,acceleration=AccelerationVector.z_direction, time=time),
                         )
    time = time + time_interval
    xResult.append(PositionVector.x_direction)
    yResult.append(PositionVector.y_direction)
    zResult.append(PositionVector.z_direction)

    check_criteria_met = position_vector_invalid(PositionVector)




fig = p1.figure()
ax = p1.axes(projection ='3d')
ax.plot3D(xResult, yResult, zResult, 'green')
ax.set_title('Plot of Trajectory over time interval')
p1.show()
