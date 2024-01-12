######################## READ ME #########################################
# Hi I'm Fabio :p , a computer science and physics double major student at the University of Cape Town.
# I was bored one day so thought it would be cool to combine those skills and make a little simulation :3
# Enjoy !
#- November 2023
 
# A Physics Bouncing ball simulation using the vpython python module
# How to use:
# Click anywhere on screen to spawn a ball. 
# feel free to modify the gravitational acceleration (g), damping factor , and time steps (dt) and monitor the effects

#More simulations coming soon. Stay tuned !

###################### Imports #######################################
from vpython import *

########## Build world and data initialisation #######################
floor = box(pos=vector(0,0,0), size=vector(50, 0.1, 50))
balls = []
totalBalls = 0

########### Simulation parameters ##########################################
g = vector(0, -9.8, 0)     #g = 9.8 ms^-2... on earth. Look up g on other planets and simulate their gravity :0
dt = 0.01
dampingFactor = 0.9        #set to 1 for elastic bounces. The damping factor determines the factor by which the ball's velocity changes after each bounce
maxBallsOnScreen = 6       #upper bound (exclusive) for max balls allowed on screen at a time

##################### Helper Functions ################################
def move(obj):             #updates balls position and velocity vectors
    if obj.pos.y < floor.pos.y + obj.radius:
        overlap = (floor.pos.y + obj.radius) - obj.pos.y
        obj.pos.y += 1.1 * overlap  # Move the ball just above the floor to avoid overlap
        obj.velocity.y *= -dampingFactor

    obj.pos += obj.velocity * dt
    obj.velocity += g * dt

def create(event):
    ball = sphere(pos = event.pos, radius = 1, color=color.red)
    ball.velocity = vector(0, 0, 0)  
    balls.append(ball)
    global totalBalls
    totalBalls += 1

######################### Scene Listeners ###############################
scene.bind('click', create) #detect click event and spawn ball at mouse location

############################ Main Update loop ###########################
while True:
    rate(300)       
    for ball in balls:
        move(ball)
    
    if totalBalls == maxBallsOnScreen:
        # Remove existing balls from the screen
        for ball in balls:
            ball.visible = False

        # Reset arrays and counters
        balls = []
        totalBalls = 0
##############################################################################