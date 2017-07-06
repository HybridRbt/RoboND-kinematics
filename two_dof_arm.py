# Define a function to compute the arm configuration
# Note: joint1_angle is the angle counterclockwise from the link1 axis
import numpy as np

def compute_arm_config(link1_length, link2_length, joint0_angle, joint1_angle):
    # assume that joint0 is at (0,0)
    joint1_x = link1_length * np.cos(joint0_angle)
    joint1_y = link1_length * np.sin(joint0_angle)

    angle = joint0_angle + joint1_angle

    p2_x = joint1_x + link2_length * np.cos(angle)
    p2_y = joint1_y + link2_length * np.sin(angle)

    return joint1_x, joint1_y, p2_x, p2_y