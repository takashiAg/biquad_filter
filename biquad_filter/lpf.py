from . import biquad
from math import pi, sin, cos, sinh, log

class lpf():
    def __init__(self, freq_of_cut_off, sample_rate, quality_factor):
        omega = 2.0 * pi * freq_of_cut_off / sample_rate
        alpha = sin(omega) / (2.0 * quality_factor)

        self.a0 = 1.0 + alpha
        self.a1 = -2.0 * cos(omega)
        self.a2 = 1.0 - alpha
        self.b0 = (1.0 - cos(omega)) / 2.0
        self.b1 = 1.0 - cos(omega)
        self.b2 = (1.0 - cos(omega)) / 2.0

        self.init_value()
