import math     #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio
import time
import msvcrt

#THIS IS CURRENTLY CODED FOR PYTHON 2

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
    for x in xrange(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    for x in xrange(RESTFRAMES): 
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

print('Press a letter:')

def dit():
    beep(.05)

def dah():
    beep(.15)




#Morse library:

def a():
    dit() 
    dah()

def b():
    dah()
    dit()
    dit()
    dit()

def c():
    dah()
    dit()
    dah()
    dit()

def d():
    dah()
    dit()
    dit()

def e():
    dit()

def f():
    dit()
    dit()
    dah()
    dit()

def g():
    dah()
    dah()
    dit()

def h():
    dit()
    dit()
    dit()
    dit()

def i():
    dit()
    dit()

def j():
    dit()
    dah()
    dah()
    dah()

def k():
    dah()
    dit()
    dah()

def l():
    dit()
    dah()
    dit()
    dit()

def m():
    dah()
    dah()

def n():
    dah()
    dit()

def o():
    dah()
    dah()
    dah()

def p():
    dit()
    dah()
    dah()
    dit()

def q():
    dah()
    dah()
    dit()
    dah()

def r():
    dit()
    dah()
    dit()

def s():
    dit()
    dit()
    dit()

def t():
    dah()

def u():
    dit()
    dit()
    dah()

def v():
    dit()
    dit()
    dit()
    dah()

def w():
    dit()
    dah()
    dah()

def x():
    dah()
    dit()
    dit()
    dah()

def y():
    dah()
    dit()
    dah()
    dah()

def z():
    dah()
    dah()
    dit()
    dit()







while True:
    try:
        
        #note = input()
        notex = msvcrt.getch()
        note = str(notex)
        if note == 'a':
            a()

        elif note == 'b':
            b()
        
        elif note == 'c':
            c()
          
        elif note == 'd':
            d()

        elif note == 'e':
            e()

        elif note == 'f':
            f()

        elif note == 'g':
            g()

        elif note == 'h':
            h()

        elif note == 'i':
            i()

        elif note == 'j':
            j()

        elif note == 'k':
            k()

        elif note == 'l':
            l()

        elif note == 'm':
            m()

        elif note == 'n':
            n()

        elif note == 'o':
            o()

        elif note == 'p':
            p()

        elif note == 'q':
            q()

        elif note == 'r':
            r()

        elif note == 's':
            s()

        elif note == 't':
            t()

        elif note == 'u':
            u()

        elif note == 'v':
            v()

        elif note == 'w':
            w()

        elif note == 'x':
            x()

        elif note == 'y':
            y()

        elif note == 'z':
            z()

        elif note == '/':
            quit()


        #time.sleep(.15)

        else:
            print('Try again fucko')

    except ValueError:
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