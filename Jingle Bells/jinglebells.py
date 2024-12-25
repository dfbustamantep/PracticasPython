import pygame # necesario instalar pip install pygame
import time
import numpy as np # pip install numpy

# https://www.instagram.com/p/DD-rln3tj99/?img_index=1

pygame.mixer.init()

# Deifnjimos las notas de Jingle Bells
#para ls notas usamos una tupla (frecuencia en Hz,duracion en segundos)

notes = [
    (659,0.4),(659,0.4),(659,0.8),
    (659,0.4),(659,0.4),(659,0.8),
    (659,0.4),(784,0.4),(523,0.4),(587,0.4),(659,0.8),
    (698,0.4),(698,0.4),(698,0.8),(698,0.4),
    (659,0.4),(659,0.4),(659,0.8),(659,0.4),
    (587,0.4),(587,0.4),(659,0.4),(587,0.4),(784,0.8)
]


# Funcion usada para generar el sonido
def generate_sound_array(frequency,duration,sample_rate = 44100):
    t = np.linspace(0,duration,int(sample_rate*duration),False)
    wave = 0.5 * np.sin(2*np.pi*frequency*t)
    sound_array = np.int16(wave * 32767)
    stereo_sound_array = np.column_stack((sound_array,sound_array))
    return stereo_sound_array



# Llamamos a nuestra funcion generate_sound_array y con pygame reproducimos el sonido
def play_note(frequency,duration):
    sound_array = generate_sound_array(frequency,duration)
    sound = pygame.sndarray.make_sound(sound_array)
    sound.play()
    time.sleep(duration)
    pygame.mixer.stop()

#Bucle principal 
print("Playing Jingle Bells")
for note in notes:
    frquency,duration = note
    play_note(frquency,duration)
    
print("Tune finished!")

