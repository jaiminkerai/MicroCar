import matplotlib.pyplot as plt
import math
import numpy as np

def microcar(instruction_files_list, action_files_list):
    exp_h_disp = np.array([])
    exp_v_disp = np.array([])
    exp_dist = np.array([])
    act_h_disp = np.array([])
    act_v_disp = np.array([])
    act_dist = np.array([])
    for instruction_file in instruction_files_list:
        instruction_file = open(instruction_file,'r')
        h_disp = 0  
        v_disp = 0
        dist = 0
        for instruction in instruction_file:
            instruction = instruction.strip('\n').split(',')
            for i in range(1,len(instruction)):
                instruction[i] = float(instruction[i])
            meters = instruction[1]*instruction[2]
            if instruction[0] == 'N':
                h_disp += meters
                dist += meters
            elif instruction[0] == 'S':
                h_disp -= meters
                dist += meters
            elif instruction[0] == 'E':
                v_disp += meters
                dist += meters
            else:
                v_disp -= meters
                dist += meters
        exp_h_disp = np.append(exp_h_disp, h_disp)  
        exp_v_disp = np.append(exp_v_disp, v_disp)
        exp_dist = np.append(exp_dist,dist)
    instruction_file.close()
    for action_file in action_files_list:
        action_file = open(action_file,'r')
        h_disp = 0  
        v_disp = 0
        dist = 0
        for action in action_file:
            action = action.strip('\n').split(',')
            for i in range(1,len(action)):
                action[i] = float(action[i])
            meters = action[1]*action[2]
            if action[0] == 'N':
                h_disp += meters
                dist += meters
            elif action[0] == 'S':
                h_disp -= meters
                dist += meters
            elif action[0] == 'E':
                v_disp += meters
                dist += meters
            else:
                v_disp -= meters
                dist += meters
        act_h_disp = np.append(act_h_disp, h_disp)  
        act_v_disp = np.append(act_v_disp, v_disp)
        act_dist = np.append(act_dist,dist)
    action_file.close()
    return exp_h_disp, exp_v_disp, exp_dist, act_h_disp, act_v_disp, act_dist
  
def plotmicrocar(instruction_files_list, action_files_list):
    exp_h_disp, exp_v_disp, exp_dist, act_h_disp, act_v_disp, act_dist = microcar(instruction_files_list, action_files_list)
    mcar = []
    plt.subplot(2,2,3)
    for i in range(0,exp_h_disp.size):
        plt.scatter(exp_h_disp[i],exp_v_disp[i], label="mcar {}".format(i+1))
        mcar.append("mcar {}".format(i+1))
    plt.xlabel('horizontal displacement (m)')
    plt.ylabel('vertical displacement (m)')
    plt.xlim(np.amin(exp_h_disp)-10, np.amax(exp_h_disp)+10)
    plt.ylim(np.amin(exp_v_disp)-10, np.amax(exp_v_disp)+10)
    plt.title('Expected Horizontal vs. Vertical Displacement of Microcar')
    plt.grid(True, lw = 1, ls = '--', c = '.75')
    plt.legend()
    
    plt.subplot(2,2,4)
    for i in range(0,act_h_disp.size):
        plt.scatter(act_h_disp[i],act_v_disp[i],marker = 'x', label="mcar {}".format(i+1))
    plt.xlabel('horizontal displacement (m)')
    plt.ylabel('vertical displacement (m)')
    plt.xlim(np.amin(act_h_disp)-10, np.amax(act_h_disp)+10)
    plt.ylim(np.amin(act_v_disp)-10, np.amax(act_v_disp)+10)
    plt.title('Actual Horizontal vs. Vertical Displacment of Microcar')
    plt.grid(True, lw = 1, ls = '--', c = '.75')
    plt.legend()
    
    plt.subplot(2,1,1)
    plt.bar(mcar, exp_dist, align='edge',color='r',width=-0.2, label= "Expected Distance" )    
    plt.bar(mcar, act_dist, align='edge',color='c',width=0.2, label= "Actual Distance")
    plt.ylabel('Distance (m)')
    plt.ylim(0, np.amax(exp_dist)+300)
    plt.title('Expected vs. Actual Distance travelled by Microcar')
    plt.legend()
    plt.show()
    

plotmicrocar(['exp1.csv','exp2.csv'],['act1.csv','act2.csv'])
