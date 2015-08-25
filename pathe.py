#!/usr/bin/env python

import pianohat,time,signal,pygame,os

pianohat.auto_leds(True)
pygame.mixer.init()

def music(audio):
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(1)
    time.sleep(5)

def player(video):
    os.system("omxplayer -o local "+str(video))

def handle_touch(ch, evt):
    #print(ch, evt)
    if ch == 0:
        print("Film 1")
        music("seaside.mp3")
        player("Blackpool_Illuminations.mp4")
    elif ch == 2:
        print("Film 2")
        music("seaside.mp3")
        player("Blackpool_Illuminations_Ride.mp4")
    elif ch == 4:
        print("Film 3")
        music("seaside.mp3")
        player("Blackpool_Issue_Title_Pathe_Pictorial_Goes_To_The_Seaside.mp4")
    elif ch == 5:
        print("Film 4")
        music("seaside.mp3")
        player("Blackpool_Promenade_1900.mp4")
    elif ch == 7:
        print("Film 5")
        music("seaside.mp3")
        player("Camera_Takes_Easter_Holiday_AKA_Blackpool_Beach.mp4")
    elif ch == 9:
        print("Film 6")
        music("seaside.mp3")
        player("Extra_!_Blackpool_Illuminations.mp4")
    elif ch == 11:
        print("Film 7")
        music("seaside.mp3")
        player("Holiday_News_Aka_Holiday_Scenes_-_Blackpool.mp4")
    elif ch == 12:
        print("Film 8")
        music("seaside.mp3")
        player("The_Pageant_Of_Progress.mp4")
    else:
        print("Press a key on the Wurlitzer")

pianohat.on_note(handle_touch)


signal.pause()
