# Laser Diffraction Analysis

This class is for analyzing the intensity spectrum for a laser going through a single slit aperture. Using this class the intensity spectrum can be compared with the Fraunhofer and Fresnel Diffraction models. 

## Setup

Clone this repository using the terminal command:

```
git clone https://github.com/basilwong/laser-diffraction-analysis.git
```

Add all (python package)dependancies using the terminal command:

```
pip install -r requirements.txt
```

## Use Example

```
import diffractiondata

analyzer = diffractiondata.DiffractionData("example-photos//11.25.jpg", True, slit_width=0.5e-3)
analyzer.plot_picture_data()
```

The result of the above code can be viewed as below:

![alt text](https://raw.githubusercontent.com/basilwong/laser-diffraction-analysis/master/example-plots/dv-0.5.png)

# Background 

In the sections below the equations governing the Fraunhofer and Fresnel models 
are defined for a single slit aperture with a screen behind it. 

To preface the data below, the <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon" title="\Delta\upsilon" /></a> represents “nearness” of a diﬀraction pattern. In general, the Fresnel limit is the better model for large <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon" title="\Delta\upsilon" /></a> while the Fraunhofer limit is the better model for <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon&space;<<&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon&space;<<&space;1" title="\Delta\upsilon << 1" /></a>.

The equation for <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon" title="\Delta\upsilon" /></a> is as below:

<a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon&space;=&space;w\sqrt{\frac{2}{R\lambda}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon&space;=&space;w\sqrt{\frac{2}{R\lambda}}" title="\Delta\upsilon = w\sqrt{\frac{2}{R\lambda}}" /></a>

 * w is slit width
 * R is distance to the screen, which in this case is 364 cm. 	
 * λ is the wavelength of the laser
 
# Fresnel Model

The Fresnel model is the generalized version of the Fraunhhofer model. 

To get the Fresnel Model we use the equations defined by Equation 12.76 in "Classical and Modern Optics" by Daniel A. Steck as below:
 
<a href="https://www.codecogs.com/eqnedit.php?latex=I(z)&space;=&space;C\int_{\upsilon_1}^{\upsilon_2}&space;cos(\frac{\pi&space;x^2}{2})dx&space;&plus;&space;C\int_{\upsilon_1}^{\upsilon_2}&space;sin(\frac{\pi&space;x^2}{2})dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I(z)&space;=&space;C\int_{\upsilon_1}^{\upsilon_2}&space;cos(\frac{\pi&space;x^2}{2})dx&space;&plus;&space;C\int_{\upsilon_1}^{\upsilon_2}&space;sin(\frac{\pi&space;x^2}{2})dx" title="I(z) = C\int_{\upsilon_1}^{\upsilon_2} cos(\frac{\pi x^2}{2})dx + C\int_{\upsilon_1}^{\upsilon_2} sin(\frac{\pi x^2}{2})dx" /></a>

Where:

<a href="https://www.codecogs.com/eqnedit.php?latex=\upsilon_1&space;=&space;-(z&space;&plus;&space;0.5)\Delta\upsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\upsilon_1&space;=&space;-(z&space;&plus;&space;0.5)\Delta\upsilon" title="\upsilon_1 = -(z + 0.5)\Delta\upsilon" /></a>
<a href="https://www.codecogs.com/eqnedit.php?latex=\upsilon_2&space;=&space;-(z&space;-&space;0.5)\Delta\upsilon" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\upsilon_2&space;=&space;-(z&space;-&space;0.5)\Delta\upsilon" title="\upsilon_2 = -(z - 0.5)\Delta\upsilon" /></a>

# Fraunhofer Model

The Fraunhofer model is obtained in the limit of <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta\upsilon&space;<<&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta\upsilon&space;<<&space;1" title="\Delta\upsilon << 1" /></a>. The resulting equation is as below:

<a href="https://www.codecogs.com/eqnedit.php?latex=I(z)&space;=&space;C(\Delta\upsilon)^2&space;*&space;(\frac{sin(\frac{z\pi(\Delta\upsilon)^2}{2})}{\frac{z\pi(\Delta\upsilon)^2}{2}})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I(z)&space;=&space;C(\Delta\upsilon)^2&space;*&space;(\frac{sin(\frac{z\pi(\Delta\upsilon)^2}{2})}{\frac{z\pi(\Delta\upsilon)^2}{2}})^2" title="I(z) = C(\Delta\upsilon)^2 * (\frac{sin(\frac{z\pi(\Delta\upsilon)^2}{2})}{\frac{z\pi(\Delta\upsilon)^2}{2}})^2" /></a>