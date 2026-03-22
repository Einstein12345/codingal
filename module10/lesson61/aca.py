# ImplementCircuit
# Outline:
# Write a Program to solve the circuit given.
# Solve circuit using Ohm's Law

V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (Ohms): "))

I = V / R

print("Current (I) =", I, "Amps")