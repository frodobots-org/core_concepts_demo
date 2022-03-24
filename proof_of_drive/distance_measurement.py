import numpy as np
import pandas as pd
import math



def clean_data(data):
    acc_data = data[data.sensor == 'acc'].reset_index(drop=True)
    dt = [0] + list(acc_data.t_ms)
    acc_data['dt'] = np.diff(dt)/1000
    acc_data[['x_acc', 'y_acc','z_acc']] = acc_data[['x','y','z']]*9.8
    acc_data = acc_data[['x_acc','y_acc','z_acc','dt']]
    return acc_data

def calculate_velocity(array,index,accdata):
    x_acc = accdata.x_acc[index]
    y_acc = accdata.y_acc[index]
    z_acc = accdata.z_acc[index]
    dt = accdata.dt[index]
    array += dt*np.array([x_acc,y_acc,z_acc])
    return array

def calculate_displacement(velocity, index,accdata):
    dt = accdata.dt[index]
    dx = velocity[0]*dt + math.pow(dt,2)*accdata.x_acc[index]*0.5
    dy = velocity[1]*dt + math.pow(dt,2)*accdata.y_acc[index]*0.5
    dz = velocity[2]*dt + math.pow(dt,2)*accdata.z_acc[index]*0.5
    array = np.array([dx,dy,dz])
    return array

def main():
    data = pd.read_csv("sample_sensor_recordings.csv")
    acc_data = clean_data(data)
    velocity = np.array([0.0,0.0,0.0])
    total_displacement_array = np.array([0.0,0.0,0.0])
    total_displacement = 0
    for i in range(len(acc_data)):
        velocity = calculate_velocity(velocity,i,acc_data)
        displacement = calculate_displacement(velocity, i,acc_data)
        total_displacement_array += displacement
        total_displacement = math.sqrt(
            math.pow(total_displacement_array[0],2) + 
            math.pow(total_displacement_array[1],2) + 
            math.pow(total_displacement_array[2],2))
        print(total_displacement)


if __name__ == "__main__":
    main()