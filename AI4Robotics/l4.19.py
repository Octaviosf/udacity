# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

new_mean = mu
new_var = sig

for i in range(len(measurements)):
    new_mean, new_var = update(new_mean, new_var, measurements[i], measurement_sig)
    new_mean, new_var = predict(new_mean, new_var, motion[i], motion_sig)

mu = new_mean
sig = new_var

print([mu, sig])

