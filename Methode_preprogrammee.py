import  matplotlib.pyplot as plt
from scipy.integrate import trapezoid

def integrate_trapezoid_built_in(y, x=None, dx=1.0, axis=-1):
    return trapezoid(y, x=None, dx=1.0, axis=-1)