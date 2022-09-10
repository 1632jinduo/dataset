import pickle
import matplotlib.pyplot as plt
import numpy as np
grid_x = 14
grid_y = 14
def getXY(n):
    x = int(n/14)
    y = int(n%14)
    return x,y
if __name__ =='__main__':
    with open('adj','rb+') as f:
        data = pickle.load(f) # 61,48,196,196
        # inflow,outflow
        inflow = np.zeros((61,48,14,14))  
        outflow = np.zeros((61,48,14,14))
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                out_data = np.sum(data[i][j],0)
                in_data = np.sum(data[i][j],1)
                for n in range(in_data.shape[0]):
                    x,y = getXY(n)
                    inflow[i][j][x][y] =out_data[n]
                    outflow[i][j][x][y]=in_data[n]
        
                
        flow = np.stack((inflow,outflow),2)
        with open('chengdu_flow','wb+') as ff:
            pickle.dump(flow,ff)
        print("Successfully")
        
        