import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy.integrate

class DiffractionData:

    def __init__(self, image_name, isrgb, wavelength=632.8 * 10 ** (-9), slit_width=0.5 * 10 ** (-3), R=3.64, pic_width=0.05):
        """
        """
        self.new_image(image_name, isrgb, wavelength, slit_width, R)

    def new_image(self, image_name, isrgb, wavelength=632.8 * 10 ** (-9), slit_width=0.5 * 10 ** (-3), R=3.64, pic_width=0.05):
        """
        """
        self.image_name = image_name
        self.isrgb = isrgb
        self.wavelength = wavelength
        self.slit_width = slit_width
        self.R = R
        self.pic_width = pic_width
        self.intensity_matrix = self.__get_intensity()
        self.mid = int(len(self.intensity_matrix) / 2)
        temp = self.intensity_matrix[self.mid, :]
        shift = min(temp)
        self.image_intensity = np.subtract(temp, shift)
        self.num = len(self.image_intensity)
        self.del_v = slit_width * np.sqrt(2 / (R * wavelength))
        self.max_intensity = max(self.image_intensity)
        self.max_index = np.argmax(self.image_intensity)
        self.__shift_intensity()

        self.fraun = self.__get_fraunhoffer()
        self.fres = self.__get_fresnel()

    def __rgb_2_gray(self, rgb):
        """

        """
        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray

    def __get_intensity(self):
        """
        """
        img = cv2.imread(self.image_name)
        if self.isrgb:
            return self.__rgb_2_gray(img)
        else:
            return img

    def __shift_intensity(self):
        self.start = np.abs(int(len(self.image_intensity) / 2) - self.max_index)
        self.shifted = self.image_intensity[int(self.start):]

    def __get_fraunhoffer(self):

        max_angle = np.arctan(self.pic_width / self.R)
        k = 2.0 * np.pi / self.wavelength
        intensity = list()
        num1 = int(self.num / 2)
        num2 = self.num - num1

        for theta in np.linspace(max_angle, 1e-9, num1):
            beta= k * self.slit_width * np.sin(theta) / 2.0
            intensity.append((np.sin(beta) / beta)**2)
        for theta in np.linspace(1e-9, max_angle, num2):
            beta= k * self.slit_width * np.sin(theta) / 2.0
            intensity.append((np.sin(beta) / beta)**2)

        c = self.max_intensity / max(intensity)
        intensity = np.multiply(c, intensity)
        return intensity

    def __get_fresnel(self):

        max_angle = np.arctan(self.pic_width / self.R)
        S = lambda x:np.sin(x**2 * np.pi / 2)
        C = lambda x:np.cos(x**2 * np.pi / 2)
        intensity = list()
        num1 = int(self.num / 2)
        num2 = self.num - num1

        for i in np.linspace(-max_angle, max_angle, self.num):
            v1 = -((i / self.slit_width) + 0.5) * self.del_v
            v2 = -((i / self.slit_width) - 0.5) * self.del_v
            intensity.append(scipy.integrate.quad(S, v1, v2)[0] ** 2 + scipy.integrate.quad(C, v1, v2)[0] ** 2)

        c = self.max_intensity / max(intensity)
        intensity = np.multiply(c, intensity)

        return intensity

    def plot_picture_data(self):
        """
        """

        x  = np.linspace(0, self.num , self.num)
        minus = x[int(self.start)]
        x1 = np.subtract(x[int(self.start):], minus)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        plt.xlabel('Horizontal Pixel')
        plt.ylabel('Relative Intensity')
        plt.title(r"$\Delta\upsilon = $" + str(self.del_v))
        plt.grid()
        ax.plot(x1,self.shifted, label="Diffraction Data")
        ax.plot(x, self.fraun, label="Fraunhofer Model")
        ax.plot(x, self.fres, label="Fresnel Model")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    a = DiffractionData("11.5.jpg", True, slit_width=0.5e-3)
    a.plot_picture_data()
    a.new_image("11.25.jpg", True, slit_width=0.75e-3)
    a.plot_picture_data()
    a.new_image("11.00.jpg", True, slit_width=1e-3)
    a.plot_picture_data()
    a.new_image("10.5.jpg", True, slit_width=1.5e-3)
    a.plot_picture_data()
    a.new_image("10.jpg", True, slit_width=2e-3)
    a.plot_picture_data()
