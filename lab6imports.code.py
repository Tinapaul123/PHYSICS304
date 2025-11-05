import numpy as np
import matplotlib.pyplot as plt
print("Tina's new upload")
# ---- Pick underdamped parameters ----
m = 0.10
k = 1.0
b = 0.030

gamma  = b/m
omega0 = np.sqrt(k/m)
alpha  = gamma/2                        
assert gamma < 2*omega0 

# ---- Initial conditions ----
x0, v0 = 0.05, 0.0

# ---- Time grid ----
T0 = 2*np.pi/omega0
t_end = 10*T0
t, dt = np.linspace(0, t_end, 4000, retstep=True)

# ---- Analytical underdamped solution ----
omega_d = np.sqrt(omega0**2 - alpha**2)
A = x0
B = (v0 + alpha*A)/omega_d
x_analytical = np.exp(-alpha*t) * (A*np.cos(omega_d*t) + B*np.sin(omega_d*t))

# ---- Plot ----
plt.plot(t, x_analytical, color='orange', label="Analytical (underdamped)")
plt.title("Underdamped Oscillation (γ < 2ω₀)")
plt.xlabel("Time (s)")
plt.ylabel("Displacement x (m)")
plt.legend()
plt.show()