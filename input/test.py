# Here is where the initial conditions of the electron probe are defined
# This filename is the input parameter of the eProbe.py file

simulation_name = 'QUASI3D'
shape = 'single'
density = 1
fill = False
iterations = 100000

# Probe centered at the following initial coordinates (in c/w_p):
x_c = -2.4 # Start within region of field
y_c = 0.25#0.25
xi_c = -5.9#-8.2#-5.9

# Initial momentum
px_0 = 110 # Make sure it goes towards the screen!
py_0 = 0
pz_0 = 0

# Screen Parameters (Assume infinite in y and z)
x_s = 50

# Shape Parameters (Radius or Side Length)
s1 = 0.04# In y
s2 = 1 # In xi
