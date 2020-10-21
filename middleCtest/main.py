from soundfile import SoundFile
import pyfftw
import time
import numpy as np
import matplotlib.pyplot as plt
from helpers import *

# Opening audio file, reading frame data and sample rate, and closing file
sf = SoundFile('source.wav')
data = sf.read()
f_s = sf.samplerate
sf.close()

start = time.time()

# Builds FFTW plan from input data
my_fft = pyfftw.builders.fft(data)

# Genereating frequency values for each bin (frequencies range for 0 to sample rate)
freq_bins = [i * (f_s / my_fft.N) for i in range(1, my_fft.N+1)]

# Executing FFT
my_fft.execute()

# Finding magnitude of each frequency found
mags = np.abs(my_fft.output_array)

end = time.time()

# Showing total execution time and info about audio file and FFT
print("Time to plan and execute: {}".format(end - start))
print_SoundFile(sf)
print('-----------------------------------')
print_FFTW(my_fft)

# Start and end indicies for plotting
s_i = int(260 * (my_fft.N / f_s))
e_i = int(264 * (my_fft.N / f_s))

'''
# Generate csv file of fourier transform in you want to plot data in spreadsheet
with open("FFT_out.csv", 'w') as f:
    for i in range(my_fft.N):
        if i < my_fft.N - 1:
            f.write('{}, {},\n'.format(freq_bins[i], mags[i]))
        else:
             f.write('{}, {}'.format(freq_bins[i], mags[i]))
    
    f.close()
'''

# Plotting fourier transform data
plt.plot(freq_bins[s_i:e_i], mags[s_i:e_i])
plt.title('Frequency of Middle C')
plt.show()
