def print_FFTW(fft, show_arrays=False):
    message = \
        """ 
        N:                  {}
        simd_aligned:       {}
        input_alignment:    {}
        output_alignment:   {}
        flags:              {}
        input size:         {}
        output size:        {}
        input_shape:        {}
        output_shape:       {}
        input_strides:      {}
        output_strides:     {}
        input_dtype:        {}
        output_dtype:       {}
        direction:          {}
        axes:               {}
        """ \
        .format( \
            fft.N,                  \
            fft.simd_aligned,       \
            fft.input_alignment,    \
            fft.output_alignment,   \
            fft.flags,              \
            fft.input_array.size,   \
            fft.output_array.size,  \
            fft.input_shape,        \
            fft.output_shape,       \
            fft.input_strides,      \
            fft.output_strides,     \
            fft.input_dtype,        \
            fft.output_dtype,       \
            fft.direction,          \
            fft.axes
        )

    print(message)

    if show_arrays:
        print("Input: \n{}\n".format(fft.input_array))
        print("Output: \n{}".format(fft.output_array))
        
def print_SoundFile(sf, show_extra_info=False):
    message = \
        """
        Name:           {}
        Mode:           {}
        Sample Rate:    {}
        Frames:         {}
        Channels:       {}
        Format:         {}
        Subtype:        {}
        Endian:         {}
        Format Info:    {}
        Subtype Info:   {}
        Sections:       {}
        Closed:         {}
        """ \
        .format( \
            sf.name,           \
            sf.mode,           \
            sf.samplerate,    \
            sf.frames,         \
            sf.channels,       \
            sf.format,         \
            sf.subtype,        \
            sf.endian,         \
            sf.format_info,    \
            sf.subtype_info,   \
            sf.sections,       \
            sf.closed
        )
    
    print(message)

    if(show_extra_info):
        print(sf.extra_info)