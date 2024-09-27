# Author Mauro Zallocco, Jan 2022

from gpiozero import Button, LED, Buzzer
from signal import pause
import pygame, time, sys

#modify this path to point to the music file that you want played.
pathToMusic = "/home/pi/User/Music/something.mp3"

button = Button(2)
led = LED(25)

print("Program initializing...")

musicStarted = False
onMode = False

def allOn():
    global musicStarted
    global onMode

    print("allOn:setting onMode to True")
    onMode = True
    led.on()
    print("allOn:musicStarted=",musicStarted)
    if not musicStarted:
      musicStarted = True
      startMusic()
      if not pygame.mixer.music.get_busy():  # we are done playing music
        musicStarted = False
    else:
      pygame.mixer.music.unpause()
      
def allOff():
    global onMode
    onMode = False
    led.off()
    pygame.mixer.music.pause()

button.when_pressed = allOn
button.when_released = allOff
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(pathToMusic)

print("Ready for button push...")
led.on()

def startMusic():
  try:
    clock = pygame.time.Clock()
    pygame.mixer.music.play()
    print("pygame.mixer.music.play() returned")
  except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
    pygame.mixer.music.stop()
    print("\nPlay Stopped by user")
  except Exception:
    print("unknown error")

pause()

print("Done")
