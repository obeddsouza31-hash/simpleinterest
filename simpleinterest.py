import sys

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100

sys.stdout.write("Simple Interest = " + str(si))