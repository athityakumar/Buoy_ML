"""
data_loader
~~~~~~~~~~~~

data_loader is the function usually called by our neural network
code to load the data of Red and yellow buoy and create training,
validation and test data sets.
"""

#### Libraries
# Third-party libraries
import numpy as np


def load_data():
    # Load the data for red_buoy and yellow buoy

    red_buoy = np.array([1,0,0])
    yellow_buoy = np.array([0,1,0])
    water = np.array([0,0,1])


    red_buoy_data = open("Data/filtered_red_data.txt",'r')
    yellow_buoy_data = open("Data/filtered_yellow_data.txt",'r')
    water_data = open("Data/filtered_water_data.txt",'r')


   # Y = 0.299R + 0.587G + 0.114B
   # U = 0.492 (B-Y)
   # V = 0.877 (R-Y)

    Rdata = []
    lines = red_buoy_data.readlines()
    for line in lines:
        x = [ float(y) for y in line.split()]
        Y = 0.299*x[2] + 0.587*x[1] + 0.114*x[0]
        U = 0.492*(x[0] - Y)
        V = 0.877*(x[2] - Y)

        # Rdata.append( [ [float(x)/256 for x in line.split()],red_buoy] )
        Rdata.append( [[Y/256, U/256, V/256], red_buoy] )
    Ydata = []
    lines = yellow_buoy_data.readlines()
    for line in lines:
        x = [ float(y) for y in line.split()]
        Y = 0.299*x[2] + 0.587*x[1] + 0.114*x[0]
        U = 0.492*(x[0] - Y)
        V = 0.877*(x[2] - Y)
        # Ydata.append( [[float(x)/256 for x in line.split()],yellow_buoy] )
        Ydata.append( [[Y/256, U/256, V/256], yellow_buoy] )


    Wdata = []
    lines = water_data.readlines()
    for line in lines:
        x = [ float(y) for y in line.split()]
        Y = 0.299*x[2] + 0.587*x[1] + 0.114*x[0]
        U = 0.492*(x[0] - Y)
        V = 0.877*(x[2] - Y)        
        # Wdata.append( [[float(x)/256 for x in line.split()],water] )
        Wdata.append( [[Y/256, U/256, V/256], water] )


    data = Rdata + Ydata + Wdata
    red_buoy_data.close()
    yellow_buoy_data.close()
    water_data.close()

    # print np.shape(Rdata)
    # print np.shape(Ydata)
    # print np.shape(data)
    np.random.shuffle(data) # Random shuffling of yellow and red buoy
    N = int(len(data)*0.70)
    V = int(len(data)*0.15)
    T = len(data) - N -V

    # print N, V, T

    training_data = data[0:N]
    validation_data = data[N:N+V]
    test_data = data[N+V:N+V+T]

    return (training_data, validation_data, test_data)