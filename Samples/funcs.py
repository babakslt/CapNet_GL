import numpy as np
# get's a dict of variable names and rand format
# make and return the random numbers
# vars : {'var1_name':[min,max,count,type],
#         'var2_name,:[min,max,count,type],
#        ...}

def generate_random(vars):
    for var in vars:
        vars[var] = np.random.uniform(vars[var][0],vars[var][1],vars[var][2])
    return vars