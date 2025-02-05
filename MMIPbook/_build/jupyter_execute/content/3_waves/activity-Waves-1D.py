#!/usr/bin/env python
# coding: utf-8

# # 20 Oct 2022 - 1-Dimensional Travelling Waves
# 
# [Wave equations](https://en.wikipedia.org/wiki/Wave_equation) are common to all branches of physics. In fact, many modern research topics include some investigations that use wave theory. So useful is the concept of a wave, that we adapted it for quantum mechanics in the form of the [Schrodinger Equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation) and the position representation of the wavefunction ($\psi(x,t)$). While wildly useful and broadly applicable, we need to build up some intution and use cases for waves. We will start with the 1D wave equation:
# 
# $$\dfrac{\partial^2 f(z,t)}{dz^2} = \dfrac{1}{v^2}\dfrac{\partial^2 f(z,t)}{dt^2}$$

# As we discussed, any function of the form:
# 
# $$f(z,t) = g(z+vt)+h(z-vt)$$
# 
# solves the 1D wave equation. One way to think about this what this solution is showing is that some smooth function $g(z)$ and another smooth function $h(z)$ individually solve the wave equation if they just move to the left for $g$ and to the right for $f$. Furthermore because this PDE is linear (containing only linear derivatives of $z$ and $t$, i.e., no squares or functions of them), [superposition](https://en.wikipedia.org/wiki/Superposition_principle) holds. And we can simply add solutions together linearly to get new solutions!

# ## Travelling Wave Solutions
# 
# That is all well and good, but we need a common language. A grammar to understand our solutions. These are basis functions, they are the things we all agree on that describe the "space" of the solutions. You have seen these already in our study of normal modes. Our sinusoidal solutions, the frequencies and amplitudes of the modes themselves, provide a set of basis functions that can describe the general motion of the coupled SHOs. What's nice about that choice is that we can reproduce it because we all agree to solve the same eigenvalue problem.
# 
# For the 1D wave equation, these functions are [Travelling Wave Solutions](https://en.wikipedia.org/wiki/Periodic_travelling_wave). The describe the simplest motion of a travelling wave: single frequency oscillation over an infinite domain. There's no end points to worry about, and only one frequency. Also, it just moves to the left or to the right. You can probably see how multiple dimensions result in much more complexity. A basic traveling wave solution is:
# 
# $$f(z,t) = A cos(kz-vt+\phi)$$
# 
# You can show that this equation satisfies the wave equation. More importantly, does a linear sum do so?
# 
# **&#9989; Do this** 
# 
# Demonstrate that this proposed general solution:
# 
# $$F(z,t) = \sum_i^n A_i\:cos(k_i z - v t + \phi_i)$$
# 
# solves the wave equation.
# 

# ## Looking at Travelling Wave Solutions
# 
# Let's investigate several scenarios for travelling wave solutions:
# 
# 1. A single travelling wave 
# 2. The superposition of two waves (not close frequencies; close amplitudes)
# 3. The superposition of two waves (close frequencies; close amplitudes)
# 4. The superposition of two waves (not close frequencies; not close amplitudes)
# 5. The superposition of two waves (close frequencies; not close amplitudes)
# 6. The superposition of three waves (make adjustments to test your intuition from two waves)
# 
# Make your choices, but also vary them a bit. You can investigate things like widgets (e.g., [sliders](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)) which make this stuff more interactive, but regular plots are totally fine. 
# 
# **&#9989; Do this** 
# 
# Here is my suggestion and a challenge:
# 
# 1. Plot your solutions in 2D for a fixed location (e.g., $x=0$) for all time ($f$ vs $t$)
# 2. Plot your solutions in 2D for a given time (e.g., $t=0$) for all x ($f$ vs $x$)
# 3. Plot your solutions in 3D using the $x-y$ plane as positions vs time and using $z$ for $f$ (what does this representation buy you? Is it more or less useful than the above two?)
# 4. Challenge (animate your plots). Matplotlib can use the animation api. [Here's a simple script](https://matplotlib.org/2.0.2/examples/animation/simple_anim.html).
# 
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation ## Only if you want



# In[2]:


## your code here


# ## Another Wave Equation
# 
# The wave equation above is a canonical 1D wave equation. It can be applied in many places, but the interpretation of the function $f$ varies from model to model. It can be height, displacement, voltage, current, density, number, temperature, etc and so on.
# 
# But one of the most important "wave" equations is the Schroedinger equation.
# 
# $i\hbar|\psi(t)\rangle = H(t)|\psi(t)\rangle$
# 
# where $H(t)$ is the Hamiltonian operator, a representation of the energetics of the system, and $\psi(t)$ is the state of the quantum mechanical system. I put "wave" in quotes, because this equation typically contains only a single derivative with respect to time unlike the classical wave equation above. However, it is still a linear partial differential equation, and thus superposition continues to be a useful tool. In QM, superposition has deep implications for the nature of particle identity and statistical uncertainty. 
# 
# **We do not solve this problem in general.** The solutions to this wave equation require knowledge of $V(x)$. Let's look at a particular case of the infinite 1D well. We need some mathematical tools and approaches to make sense of it. It also needs to have a context because typically $H(t)$ should be known.
# 
# Our to this problem is solve for "steady state" solutions, those that do not depend on time. For many quantum systems, the time evolution of these stationary states turns out to be quite simple. Typically it involves multiplying the stationary state by a time evolving phase that is proportional to the energy of the state ($e^{iE_nt/\hbar}$).
# 
# 

# ### The 1D Infinite Square Well
# 
# There's a lot that goes into describing how we get from the general Schroedinger equation to the one below. Books start from this differential equation below calling it the "Schroedinger equation", but it is really the position representation of the energy eigenvalue problem. Which is a mouthful. But basically this only solves for stationary states, and will give us the energy of those states. Anything more general has to be built from these eigenstates.
# 
# Because we have indicated we are interested in steady state solutions, those tend to be energy eigenstates of the system. That is, the solutions to the steady state problems ae the basis functions for general states! With this, our work becomes solving the following 1D differential equation:
# 
# $$\dfrac{\hbar^2}{2m}\dfrac{\partial^2 \phi_E(x)}{\partial x^2} + V(x)\phi_E(x) = E\phi_E(x)$$
# 
# where $\phi_E(x)$ represents the position representation of a given energy eigenstate. This is not the Schroedinger equation, but rather an instance of it's use in this problem where we seek stationary soltuions. Notice there is a new linear potential term in the equation $V(x)$. 
# 
# A 1D infiite well has a potential $V(x)=0$ over a range and is otherwise zero.
# 
# $$V(x) = 0\;\mathrm{from}\; 0<x<a \; \mathrm{and}\:\infty\:\mathrm{otherwise}$$
# 
# Thus inside the box we have:
# 
# $$\dfrac{\hbar^2}{2m}\dfrac{\partial^2 \phi_E(x)}{\partial x^2} = E\phi_E(x)$$
# 
# And outside the box, $\phi_E(x)$ must vanish because $V(x)=\infty$ there.
# 
# Let's solve for $\phi_E(x)$ and $E$ and see what this "wave" equation indicates.
# 
# 
# 

# ## Resources
# 
# Much of what we are discussing about waves appears in the following sets of notes:
# 
# * [Introduction to Waves](https://dannycaballero.info/phy482msu_s2020/notes/handwritten/09-Introduction_to_waves.pdf)
# * [Electromagnetic Waves in Vacuum](https://dannycaballero.info/phy482msu_s2020/notes/handwritten/10-Electromagnetic_waves.pdf)
# * [The Wavefunction](https://dannycaballero.info/phy472msu_s2021/notes/handwritten/04%20-%20Wavefunctions.pdf)
# * [The 1D Infinite Square Well](https://dannycaballero.info/phy472msu_s2021/notes/handwritten/05%20-%20Infinite%20Square%20Well.pdf)

# 
