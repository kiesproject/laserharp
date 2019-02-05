from kyori import *
from musicplay import musicplay
import subprocess

while True:
    if((reading(0,13,11)+reading(0,13,11))/2 < 10):
        musicplay("pianoC.mp3")

    if((reading(0,18,16)+reading(0,18,16))/2 < 10):
        musicplay("pianoD.mp3")
