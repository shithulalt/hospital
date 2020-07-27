from time import time,strftime,sleep
from pygame import mixer
from datetime import datetime


def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def IsOfficeTime(currenttime):
    if currenttime > '09:00:00' and currenttime < '18:00:01':
        return True
    else:
        return False

def log_now(msg):
    with open("myrecords.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")




NumberofWaterRemaining = 18

WaterAfterEvery = 1200  # Seconds  - 20 minutes
EyeExerciseAfterEvery = 1800  # Seconds - 30 minutes
PhysicalExerciseAfterEvery = 2700  # Seconds  - 45 minutes

#waterMp3 = 'water.mp3'
#eyesMp3 = 'water.mp3'
#PhysicalMp3 = 'water.mp3'

currenttime = strftime('%H:%M:%S')
WaterTakenAt = time()
EyeExerciseAt = time()
PhysicalExerciseAt = time()

SleepTime = 1200  # Sleep time in seconds It will check after every 60 seconds.

while (IsOfficeTime(currenttime)):
    #     Check for water
    if NumberofWaterRemaining > 0:
        if time() - WaterTakenAt > WaterAfterEvery:  # water after every 20 minutes
            print("Time to drink water \nEnter Done if you had water:-->")
            while True:
                playMusic('water.Mp3','done')
                WaterTakenAt = time()
                log_now("Drank Water at")
                NumberofWaterRemaining -= 1
                break
        if time() - EyeExerciseAt > EyeExerciseAfterEvery:
            print("Time to do eye exercise \nEnter Done if you done eye exercise-->")
            while True:
                playMusic('water.Mp3','done')
                EyeExerciseAt = time()
                log_now("Eyes exercise did at")
                break
        if time() - PhysicalExerciseAt > PhysicalExerciseAfterEvery:
            print("Time to do Physical exercise \nEnter Done if you done Physical exercise --->")
            while True:
                playMusic('water.Mp3','done')
                PhysicalExerciseAt = time()
                log_now("Physical Activity done at")
                break

    sleep(SleepTime)
    currenttime = strftime('%H:%M:%S')