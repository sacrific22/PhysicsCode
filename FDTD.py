import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pathlib import Path
# Simulation parameters
N = 200             # number of E nodes (number of Segments) (integer grid points 0..N-1)
dx = 1.0            # spatial step (arbitrary units)
c = 1.0             # speed of light (normalized)
S = 0.99            # Courant number (must be <= 1 for stability in 1D with c=1)
dt = S * dx / c     # time step
Nt = 800            # total number of time steps to simulate
snap_every = 4      # store snapshot every this many steps (for animation)
# Fields (arrays)
E = np.zeros(N, dtype=float)     # E at integer grid points 0..N-1
H = np.zeros(N - 1, dtype=float) # H at half-integer points between E nodes
# Source (soft Gaussian pulse)
src_pos = N // 2      # injection index for E
t0 = 40.0             # pulse center in time steps
spread = 12.0         # pulse width
# Precompute coefficient
coef = dt / dx        # appears in discrete derivatives
# Storage for snapshots
snapshots = []
x = np.arange(N) * dx
# Time-stepping loop
for n in range(Nt):
    # 1) Update H (magnetic field) using current E
    # H[i]^(n+1/2) = H[i]^(n-1/2) - (dt/dx) * (E[i+1]^n - E[i]^n)
    H -= coef * (E[1:] - E[:-1])
    # 2) Update E (electric field) using updated H
    # E[i]^(n+1) = E[i]^n - (dt/dx) * (H[i]^(n+1/2) - H[i-1]^(n+1/2))
    # update only interior nodes; boundary nodes handled below (PEC)
    E[1:-1] -= coef * (H[1:] - H[:-1])
    # 3) Enforce PEC boundaries (perfect electric conductor)
    E[0] = 0.0
    E[-1] = 0.0
    # 4) Add source (soft Gaussian in time) at src_pos (adds to E)
    src = np.exp(-0.5 * ((n - t0) / spread) ** 2)
    E[src_pos] += src
    # 5) Save snapshots periodically for animation
    if (n % snap_every) == 0:
        snapshots.append(E.copy())
# Create and save animation
fig, ax = plt.subplots(figsize=(9, 3.5))
ax.set_xlim(0, (N - 1) * dx)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel('x (grid index × dx)')
ax.set_ylabel('E (normalized)')
line, = ax.plot(x, snapshots[0], lw=1.5)
ax.set_title('1D FDTD — E-field (PEC boundaries), c=1, N=200')

def animate(i):
    line.set_ydata(snapshots[i])
    ax.set_title(f'1D FDTD — E-field — time step: {i * snap_every}')
    return (line,)

ani = animation.FuncAnimation(fig, animate, frames=len(snapshots), interval=30, blit=True)
gif_path = Path('fdtd_1d.gif')
ani.save(gif_path, writer='pillow', fps=30)
plt.close(fig)
# Save a preview snapshot (first saved frame)
fig2, ax2 = plt.subplots(figsize=(9, 3.5))
ax2.plot(x, snapshots[0], lw=1.3)
ax2.set_xlim(0, (N - 1) * dx)
ax2.set_ylim(-1.2, 1.2)
ax2.set_xlabel('x (grid index × dx)')
ax2.set_ylabel('E (normalized)')
ax2.set_title('1D FDTD — sample snapshot (first frame)')
preview_path = Path('fdtd_1d_snapshot.png')
fig2.savefig(preview_path, bbox_inches='tight')
plt.close(fig2)
print(f"Animation saved to: {gif_path.resolve()}")
print(f"Preview snapshot saved to: {preview_path.resolve()}")
