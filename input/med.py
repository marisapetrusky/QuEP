# Here is where the initial conditions of the electron probe are defined
# This filename is the input parameter of the eProbe.py file

simulation_name = 'QUASI3D'
shape = 'ribbon'
density = 100
iterations = 10000

# Probe centered at the following initial coordinates:
x_c = -2.4 # Start within region of field
y_c = 0.25
xi_c = -12

# Initial momentum
px_0 = 6 # Make sure it goes towards the screen!
py_0 = 0
pz_0 = 0

# Screen Parameters (Assume infinite in y and z)
x_s = 40

# Shape Parameters (Radius or Side Length)
s1 = 1# In y
s2 = 1 # In xi
