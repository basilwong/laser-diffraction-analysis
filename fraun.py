#   fraun.py
#    Single Slit Diffraction
#    Fraunhofer diffraction intensity
from pylab import *
from math import *

lamb = 0.5 * 10**(-6)   # wavelength (m)  500 nm
k=2.0*pi/lamb
d = 0.1*10**(-3)        # slit width  (m)
dmm = d * 1000.0        # slit width  (mm)
lambnm=lamb*10**9       # wavelength  (nm)

num=500                 # number of points
inten=zeros(num)
thetx=zeros(num)
for ithet in range(1,num):
        thet = ithet/(50.0*num)               # angle (radians)
        beta=k*d*sin(thet)/2.0
        print(beta)
#        inten[ithet]=sinc(beta/pi)**2        # Alternative: intensity
        inten[ithet]=(sin(beta)/beta)**2      # Intensity
        thetx[ithet]=thet                     # angle
plot(thetx,inten,'b-')
title('slit width=%4.2f mm     wavelength=%5.0f nm ' % (dmm,lambnm))
xlabel(' theta')
ylabel(' Intensity')
grid()
show()
