<h1 align="left">1D FDTD Animation</h1>

###

<h6 align="left">members:<br>Mastov Boris</h6>

###

<h2 align="left">About project</h2>

###

<h3 align="left">Main idea of code</h3>

###

<h6 align="left">Solve Maxvell equation on grid in terms of time and space in 1 Dimesion<br>​</h6>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/f1.jpg"  />
</div>

###

<h6 align="left">E(x,t) — Electric field,<br><br>H(x,t) — magnetic field.<br><br>Fields E and H calculated sequentially in tima on Yee grid</h6>

###

<h2 align="left">Paramaters</h2>

###

<h6 align="left">N = 200: number of nodes for the electric field (essentially, the length of the line).<br><br>dx = 1: spatial step (cell length).<br><br>c = 1: speed of light normalized for simplicity.<br><br>S = 0.99: Courant number, which determines stability. Must be ≤ 1.<br><br>dt = S * dx / c: time step (according to Courant's condition).<br><br>Nt = 800: number of time steps.<br><br>snap_every = 4: save every 4th step for animation.</h6>

###

<h3 align="left">Defining Fields</h3>

###

<h6 align="left">E = np.zeros(N)<br>H = np.zeros(N - 1)<br><br>E stores the values of the electric field at the integer nodes of the grid.<br><br>H stores the values at the half nodes between them.<br><br>This is the standard FDTD grid structure: the fields alternate.</h6>

###

<h3 align="left">Source (wave excitation)</h3>

###

<h6 align="left">src_pos = N // 2<br>t0 = 40.0<br>spread = 12.0<br>Source shape — Gaussian pulse (soft, smooth start):</h6>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/f2.jpg"  />
</div>

###

<h3 align="left">Magnetic field update H</h3>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/f3.jpg"  />
</div>

###


<h6 align="left">This is the discrete form of Maxwell's equation for H</h6>

###


###

<h3 align="left">Magnetic field update H</h3>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/f4.jpg"  />
</div>

###

<h6 align="left">Discrete form too!<br>We only update internal nodes because there are special conditions at the edges.</h6>

###
<h3 align="left">Magnetic field update H and E for something with ε>1</h3>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/f5.jpg"  />
</div>

###

<h6 align="left">Since we  normalized c=1 and μ=1, we can handle materials by assigning different values of 𝜀i, For free space: 𝜀=1 , For dielectric: 𝜀>1</h6>
###
<h3 align="left">Boundary conditions (PEC — perfectly conducting boundaries)</h3>

###

<h6 align="left">E[0] = 0.0<br>E[-1] = 0.0<br><br>That means that on the edges(ends) of line E equals to zero<br>When the wave reaches the end, it is reflected with a phase inversion.</h6>

###

<h3 align="left">Adding a source</h3>

###

<h6 align="left">src = np.exp(-0.5 * ((n - t0) / spread) ** 2)<br>E[src_pos] += src<br><br>We add a small electric field pulse to the center of the grid.<br>It triggers a wave that will travel in both directions.</h6>

###

<h2 align="left">Result</h2>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d.gif"  />
</div>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d_snapshot.png"  />
</div>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d_dielectric.gif"  />
</div>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d_dielectric_snapshot.png"  />
</div>

###

<h6 align="left">The GIF file shows how the electric field <br>E(x,t) propagates in both directions from the center,<br>reflecting from the ends with a phase shift.<br><br>This is the simplest visualization of the wave equation in 1D using FDTD.</h6>

###


<h3 align="left">Extras</h3>
###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d_dielectric_with_slab_and_higher_e_region.gif"  />
</div>

###

<div align="center">
  <img height="200" src="https://github.com/sacrific22/PhysicsCode/blob/main/fdtd_1d_dielectric_snapshot_slab.png"  />
</div>

###

<h6 align="left">added dielectric slab in the middle and made higher e region in the end eps_r[80:120] = 2.5 (this is slab) eps_r[150:] = 5.0 (this is higher region)</h6>

###


<h2 align="left">Coded on</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

###

<h2 align="left">Before using code:</h2>

###

<p align="left">pip install numpy<br>pip install matplotlib</p>

###
