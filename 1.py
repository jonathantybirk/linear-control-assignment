#%%
import sympy as sp

# Symbols
s = sp.symbols('s')

# Parameters
C = 0.1
J1, J2, J3 = 0.0025, 0.0018, 0.0018
b1, b2, b3 = 0.0023, 0.0002, 0.0001
k1, k2     = 2.7, 2.6

# Blocks
c1 = J1*s**2 + b1*s + k1
c2 = J2*s**2 + b2*s + (k1 + k2)
c3 = J3*s**2 + b3*s + k2

# Closed-loop characteristic polynomial (unity feedback)
Dcl = c1*(c2*c3 - k2**2) - k1**2*c3 #+ C*k1*k2

display(sp.expand(Dcl))

sp.nroots(Dcl.subs(C,-1))


# %%
