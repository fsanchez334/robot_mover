# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:07:40 2021

@author: ferna
"""
import math
from matplotlib import path
def m_line(starting, goal): #Back up in order to get on track 
    m = (goal[1] - starting[1]) / (goal[0] - starting[0])
    m_x = m * goal[0]
    b = goal[1] - m_x
    
    print("y =" +  str(m) + "x" + "+ "+  str(b));
    

def unit_vector(vector, step):
    nudge = math.sqrt((vector[0] ** 2) + (vector[1] **2))
    unit = [nudge *vector[0], nudge *vector[1]]
    result = [step * unit[0], step * unit[1]];
    return result

def bug2_algorithm(starting, endpoint, step, obstacle):
    vector = [endpoint[0] - starting[0], endpoint[1] - starting[1]]
    unit = unit_vector(vector, step)
    updated_position = [starting[0] + unit[0], starting[1] + unit[1]]
    
    obstacle = path.Path(obstacle)
    print(updated_position)
    must_change = obstacle.contains_points([(updated_position)])
    return must_change

ball_coordinate = (1, 0)
goal = (21, 20)
step = 0.012
obstacle= [(6,10), (9, 10), (6, 1), (9,1)]
print(ball_coordinate)
print(m_line(ball_coordinate, goal))
print(bug2_algorithm(ball_coordinate, goal, step, obstacle))

p = path.Path([(0,0), (0, 1), (1, 1), (1, 0)])  # square with legs length 1 and bottom left corner at the origin
print(p.contains_points([(.5, .5)]))

'''
Next steps:
    Create rotate function
    Have a function that calculates the point updated position and sees if it would intersect
    If it does, return that you cannont
'''