import math
import random
import sys

sys.path.insert(0,'./reiforcement_learning')
sys.path.insert(0,'./bayesian')

import sonar
import sonar_array
import constants
import utils
import robot
import baysian_obs_avoid

# define constants
FRAME_SIZE = 500
N_SENSOR = 16 
N_OBSTACLES = 16
N_EPISODES = 10

def create_random_escalar():
    return random.randint(0,FRAME_SIZE)

def create_random_position():
    return [create_random_escalar(), create_random_escalar()]

def create_random_setup():
    robot_pos = create_random_position()
    goal_pos = create_random_position()
    full_obstacle_list = []
    for _ in range(N_OBSTACLES):
        full_obstacle_list.append((create_random_escalar(),create_random_escalar()))
    return robot_pos, goal_pos, full_obstacle_list

def play_episode():
    robot_co = 1

    robot_pos, goal_pos, full_obstacle_list = create_random_setup()
    print (f"robot_pos={robot_pos}")
    print (f"goal_pos={goal_pos}")
    print (f"full_obstacle_list={full_obstacle_list}")

    #create a sonar array
    r1 = robot.Robot(robot_pos, robot_co, N_SENSOR, goal_pos)
    r2 = baysian_obs_avoid.Robot(robot_pos, robot_co, N_SENSOR, goal_pos)


    step_number1 = 1
    hit_obstcle1, reach_goal1 = False, False
    # Experiment 1
    while (hit_obstcle1 == False and reach_goal1 == False):
        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("")
        print(f"step_number={step_number1}")
        hit_obstcle1, reach_goal1 = r1.update(full_obstacle_list, goal_pos) 
        step_number1 += 1
    print(f"Completed in {step_number1} steps")
    
    step_number2 = 1
    hit_obstcle2, reach_goal2 = False, False
    # Experiment 1
    while (hit_obstcle2 == False and reach_goal2 == False):
        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("")
        print(f"step_number={step_number2}")
        hit_obstcle2, reach_goal2 = r2.update() 
        step_number2 += 1    
    print(f"Completed in {step_number2} steps")
    return step_number1, hit_obstcle1, reach_goal1, step_number2, hit_obstcle2, reach_goal2



episodes_data = {    
    "episode" : [],
    "steps1" : [],
    "success1" : [],
    "steps2" : [],
    "success2" : []
}

for i in range(N_EPISODES):
    step_number1, hit_obstcle1, reach_goal1,step_number2, hit_obstcle2, reach_goal2  = play_episode()
    episodes_data["episode"].append(i)
    episodes_data["steps1"].append(step_number1)
    episodes_data["success1"].append(reach_goal1)
    episodes_data["steps2"].append(step_number2)
    episodes_data["success2"].append(reach_goal2)

print("Final result")
print("------------")
print("Episode: ", episodes_data["episode"])
print("Steps1: ", episodes_data["steps1"])
print("Success1: ", episodes_data["success1"])
print("Steps2: ", episodes_data["steps2"])
print("Success2: ", episodes_data["success2"])
