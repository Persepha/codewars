def wave(str):
    mexican_wave = []

    wave_length = len(str)
    for i in range(wave_length):
        if str[i] == ' ':
            continue
        mexican_wave.append(str[:i] + str[i].upper() + str[i+1:])
        
    return mexican_wave