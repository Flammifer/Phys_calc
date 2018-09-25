import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def linear_f(x, a, b):
def parabola(x, a, b, c):
    return a*x*x+b*x+c;


neon_x  = np.array([2606 , 2576 , 2508 , 2490 , 2464 , 2390 , 2280 , 2248 , 2146 , 1884])
neon_y = np.array([703.0 , 692.9 , 671.7 , 667.8 , 659.9 , 640.2 , 614.3 , 607.4 , 585.2 , 540.1])
x_sigma_n = np.array([5.0]*10)
popt_n, pcov_n, = curve_fit(linear_f, neon_x, neon_y, sigma = x_sigma_n)
print("NEON")
print(popt_n[0], "+-",  np.sqrt(pcov_n[0,0]))
print(popt_n[1], "+-",  np.sqrt(pcov_n[1,1]))
t = np.linspace(300, 2700, 100)


hg_x = np.array([2574 , 2318 , 2114 , 2104 , 1922 , 1504 , 846 , 302 ])
hg_y = np.array([690.7 , 623.4 , 579.1 , 577.0 , 546.1 , 491.6 , 435 , 404.7])
x_sigma = np.array([5.0]*8)
popt_hg, pcov_hg, = curve_fit(parabola, hg_x, hg_y, sigma = x_sigma)
print("HG")
print(popt_hg[0], "+-",  np.sqrt(pcov_hg[0,0]))
print(popt_hg[1], "+-",  np.sqrt(pcov_hg[1,1]))
print(popt_hg[2], "+-",  np.sqrt(pcov_hg[2,2]))
fig = plt.figure()
ax1 = fig.subplots()

#ax1.errorbar(neon_x, neon_y,  xerr = x_sigma_n, fmt = 'r')
ax1.plot(t, np.polyval(popt_n, t), 'r' )
ax1.errorbar(hg_x, hg_y,  xerr = x_sigma, fmt = '.')
ax1.plot(t,  np.polyval(popt_hg, t), 'b')
ax1.errorbar(neon_x, neon_y,  xerr = x_sigma_n, fmt='.')
ax1.set_xlabel("Monochromator scale, degrees")
ax1.set_ylabel("Wavelength, nm")

ax1.axvline(x=2406)
ax1.axvline(x=1450)
ax1.axvline(x=808)
ax1.axvline(x=410)
ax1.axvline(x=2338, color='red')
ax1.axvline(x=2288, color='red')
ax1.axvline(x=1588, color='red')
plt.grid(True)
plt.show()