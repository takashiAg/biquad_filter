from math import pi, sin, cos, sinh, log, sqrt


class biquad:
    def init_value(self):
        self.input_1 = 0
        self.input_2 = 0
        self.output_0 = 0
        self.output_1 = 0
        self.output_2 = 0

    def Biquad(self, input_0):
        output_0 = self.b0 / self.a0 * input_0 \
                   + self.b1 / self.a0 * self.input_1 \
                   + self.b2 / self.a0 * self.input_2 \
                   - self.a1 / self.a0 * self.output_1 \
                   - self.a2 / self.a0 * self.output_2
        self.input_2 = self.input_1
        self.input_1 = input_0
        self.output_2 = self.output_1
        self.output_1 = output_0
        return output_0

    def update(self, input):
        output = self.Biquad(input)
        return output


class lpf(biquad):
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


class hpf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, quality_factor):
        omega = 2.0 * pi * freq_of_cut_off / sample_rate
        alpha = sin(omega) / (2.0 * quality_factor)

        self.a0 = 1.0 + alpha
        self.a1 = -2.0 * cos(omega)
        self.a2 = 1.0 - alpha
        self.b0 = (1.0 + cos(omega)) / 2.0
        self.b1 = -(1.0 + cos(omega))
        self.b2 = (1.0 + cos(omega)) / 2.0

        self.init_value()


class bpf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, band_width):
        omega = 2.0 * pi * freq_of_cut_off / sample_rate
        alpha = sin(omega) * sinh(log(2.0) / 2.0 * band_width * omega / sin(omega))

        self.a0 = 1.0 + alpha
        self.a1 = -2.0 * cos(omega)
        self.a2 = 1.0 - alpha
        self.b0 = alpha
        self.b1 = 0.0
        self.b2 = -alpha

        self.init_value()


class brf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, band_width):
        omega = 2.0 * pi * freq_of_cut_off / sample_rate
        alpha = sin(omega) * sinh(log(2.0) / 2.0 * band_width * omega / sin(omega))

        self.a0 = 1.0 + alpha
        self.a1 = -2.0 * cos(omega)
        self.a2 = 1.0 - alpha
        self.b0 = 1.0
        self.b1 = -2.0 * cos(omega)
        self.b2 = 1.0

        self.init_value()


class lsf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, quality_factor, gain):
        omega = 2.0 * 3.14159265 * freq_of_cut_off / sample_rate
        alpha = sin(omega) / (2.0 * quality_factor)
        A = pow(10.0, (gain / 40.0))
        beta = sqrt(A) / quality_factor

        self.a0 = (A + 1.0) + (A - 1.0) * cos(omega) + beta * sin(omega)
        self.a1 = -2.0 * ((A - 1.0) + (A + 1.0) * cos(omega))
        self.a2 = (A + 1.0) + (A - 1.0) * cos(omega) - beta * sin(omega)
        self.b0 = A * ((A + 1.0) - (A - 1.0) * cos(omega) + beta * sin(omega))
        self.b1 = 2.0 * A * ((A - 1.0) - (A + 1.0) * cos(omega))
        self.b2 = A * ((A + 1.0) - (A - 1.0) * cos(omega) - beta * sin(omega))

        self.init_value()


class hsf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, quality_factor, gain):
        omega = 2.0 * 3.14159265 * freq_of_cut_off / sample_rate
        alpha = sin(omega) / (2.0 * quality_factor)
        A = pow(10.0, (gain / 40.0))
        beta = sqrt(A) / quality_factor

        self.a0 = (A + 1.0) - (A - 1.0) * cos(omega) + beta * sin(omega)
        self.a1 = 2.0 * ((A - 1.0) - (A + 1.0) * cos(omega))
        self.a2 = (A + 1.0) - (A - 1.0) * cos(omega) - beta * sin(omega)
        self.b0 = A * ((A + 1.0) + (A - 1.0) * cos(omega) + beta * sin(omega))
        self.b1 = -2.0 * A * ((A - 1.0) + (A + 1.0) * cos(omega))
        self.b2 = A * ((A + 1.0) + (A - 1.0) * cos(omega) - beta * sin(omega))

        self.init_value()


class pkf(biquad):
    def __init__(self, freq_of_cut_off, sample_rate, bw, gain):
        omega = 2.0 * 3.14159265 * freq_of_cut_off / sample_rate
        alpha = sin(omega) * sinh(log(2.0) / 2.0 * bw * omega / sin(omega))
        A = pow(10.0, (gain / 40.0))

        self.a0 = 1.0 + alpha / A
        self.a1 = -2.0 * cos(omega)
        self.a2 = 1.0 - alpha / A
        self.b0 = 1.0 + alpha * A
        self.b1 = -2.0 * cos(omega)
        self.b2 = 1.0 - alpha * A

        self.init_value()
