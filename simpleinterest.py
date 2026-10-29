import sys

p = float(sys.argv[1])
r = float(sys.argv[2])
t = float(sys.argv[3])

si = (p * r * t) / 100

print("Principal amount:", p)
print("Rate of interest:", r)
print("Time:", t)
print("Simple Interest:", si)