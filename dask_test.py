import numpy as np
from dask import delayed

def bootstrap_dask(data, boots):
    """
    Create bootstrap datasets that represent the distribution of the mean.
    Returns a numpy array containing the bootstrap datasets 
    
    Keyword arguments:
    data -- numpy array of systems to boostrap
    boots -- number of bootstrap (default = 1000)
    
    DOESN't Work.  Had to switch from numpy array to list
    End up with a an array of delayed objects rather.
    """
        
    #to_return = np.empty(boots)
    d = []
    total=0.0
                
    for b in range(boots):
        mn = bs_mean(data)
        d.append(mn)
    
    return d
    
    
@delayed
def bs_mean(data):
    total = 0
    for s in range(data.shape[0]):
        total += draw_sample(data)
    return total / data.shape[0]
    
@delayed
def draw_sample(data):
    u = np.random.uniform(0, data.shape[0]-1)
    u = round(u)
    return data[u]
    
    
