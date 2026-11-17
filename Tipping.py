from fitting_functions import *
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

def new_func(bill_amount,tip_amount):
    return (tip_amount/bill_amount)*100

data = np.loadtxt("tips.csv", delimiter=",", dtype=str)

x = data[1:, 0].astype(np.float32) # I did this one for you
y = data[1:, 1].astype(np.float32)

print("y=",y)
print("x=",x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(x,y)
plt.plot(x,linear(x,slope,intercept),label='linear fit')
plt.xlabel('Bills($)')
plt.ylabel('Tips($)')
plt.show()

print_equation(slope,intercept,'$','$')
fig.savefig('dataplot_1.png') # Please use this command to save your plots as PNG files
#The equation of the line is y = 0.18221473222560391 $/$ x + -0.2922674195507699 $



z=data[1:,6]
z = data[1:, 6].astype(np.float32)
print("z=",z)
print("x=",x)

params, params_cov = scipy.optimize.curve_fit(linear, x, z)
slope = params[0]
intercept = params[1]
fig = plt.figure()
plt.scatter(x,z)
plt.plot(x,linear(x,slope,intercept),label='linear fit')
plt.xlabel('Bills($)')
plt.ylabel('PctTip(%)')
plt.show()
print_equation(slope,intercept,'%','$')
fig.savefig('dataplot_2.png') 

