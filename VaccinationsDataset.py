# The dataset contains the following numbers:
# never: 5
# once: 8
# twice: 4
# 3 times: 3
# Calculate and output the variance.

# ds = [14, 18, 19, 24, 26, 33, 42, 55, 67]
ds = [8, 4, 4, 3, 3, 3]
c = len(ds)
t = 0
for i in range(c):
    t += ds[i]
variance = 0
dt = 0.0
m = t / c
for i in range(c):
    dt += (ds[i] - m)**2
variance = dt/c
print(ds, ": ", c, "\nMean: ", m, "\nVariance:", variance, "Dt: ", dt)
