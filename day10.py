import numpy as np
import pandas as pd

t = int(input())

for i in range(t):
    i = input()

    data_frame = pd.DataFrame(np.array([input().split() for i in range(6)], float).T)
    
    print(data_frame.corr('kendall')[0][1:].idxmax())
