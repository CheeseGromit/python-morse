import math     #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import time
import msvcrt

#THIS IS IN THE PROCESS OF BECOMING COMPATIBLE WITH PYTHON 3

PyAudio = pyaudio.PyAudio     #initialize pyaudio

def beep(LENGTH):
    #See http://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 16000     #number of frames per second/frameset.      

    FREQUENCY = 1500     #Hz, waves per second, 261.63=C4-note.
    #LENGTH = .05     #seconds to play sound

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY+100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''    

    #generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()



    stream = p.open(format = p.get_format_from_width(1), 
                    channels = 1, 
                    rate = BITRATE, 
                    output = True)

    stream.write(WAVEDATA)
    #time.sleep(.05)
    #stream.write(WAVEDATA)
    

counter1 = 0  #counters for SOS when 3 is pressed
counter2 = 0
counter3 = 0

def dit():
    beep(.05)

def dah():
    beep(.15)


#morse library:





while True:
    try:
        print('Press 1 or 2:')
        #note = input()
        note = msvcrt.getwch()
        #note = str(notex)
        if note == 'a':
            dit()

        elif note == 's':
            dah()
        
        elif note == 'd':
            while counter1 < 3:
                dit()
                counter1 = counter1 + 1
            while counter2 < 3:
                dah()
                counter2 = counter2 + 1
            while counter3 < 3:
                dit()
                counter3 = counter3 + 1   

            counter1 = 0
            counter2 = 0
            counter3 = 0 
        elif note == 'f':
            quit()
        else:
            print('Try again fucko')

    except ValueError:
        print('Error, do you want to quit? Y for yes')
        query = input()
        #query = msvcrt.getch()
        #query = str(query)
        if query == 'y':
            quit()
        else:
            print('')


#while True:
    #note = input()
    #stream.write(WAVEDATA)
    #print('press a key')
    #raw_input()
    #stream.write(WAVEDATA)
    






stream.stop_stream()

stream.close()







p.terminate()