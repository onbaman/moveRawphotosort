import os
import sys
import shutil
import time

# Create a GUI system
# In Alpha .5 clean up the system and functionalize. Cleaned up the code a little bit more

print('{:*^62}'.format("*"))
print('*{:^60}*'.format('Welcome to moveRaw'))
print('*{:^60}*'.format('Version Alpha 0.5'))
print('*{:^60}*'.format('By Vinh Huynh'))
print('{:*^62}\n'.format("*"))


def update_progress(progress):
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength * progress))
    text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), round(progress * 100), status)
    sys.stdout.write(text)
    sys.stdout.flush()


# User input that checks to see what raw type you want sorted
def camera_type():
    validRaw = False  # validation checker
    while validRaw is False:
        cameraType = input("Input:")
        # cameraType = input("Input:")
        if cameraType is '1':
            return '.CR2'
            validRaw = True
        elif cameraType is '2':
            return '.NEF'
            validRaw = True
        elif cameraType is '3':
            return '.ARW'
            validRaw = True
        elif cameraType is '4':
            return '.RW2'
            validRaw = True
        elif cameraType is '5':
            return '.ORF'
            validRaw = True
        elif cameraType is '6':
            return '.RAW'
            validRaw = True
        else:
            print("Invalid Input Try again")


print('{:*^62}'.format('Select a Camera Brand'))
print(' {:<20}'.format("1:Canon") + '{:^20}'.format("2:Nikon") + '{:>20} '.format('3:Sony'))
print(' {:<20}'.format("4:Panasonic(Lumix)") + '{:^20}'.format("5:Olympus") + '{:>20} '.format('6:FujiFilm'))
print('{:*^62}'.format("*"))

rawType = camera_type()

validDir = False
jpegVector = []
rawVector = []

# Check if file directory exists
while validDir is False:
    filePath = input('Please enter the destination you would like to sort: ')
    if os.path.isdir(filePath):
        # print("This exists")
        validDir = True
    else:
        print("Error please try again")
jpeg = filePath + '/JPEG'
raw = filePath + '/RAW'

# Check if a JPEG and Raw folder are already created, if false make new folders
if os.path.exists(jpeg) and os.path.exists(raw):
    print("You have two folders prepared")
if not os.path.exists(jpeg):
    os.makedirs(jpeg);
else:
    print("JPEG folder exists")
if not os.path.exists(raw):
    os.makedirs(raw)
else:
    print("RAW folder exists")

# Scan through the directory and count the number of raw and jpeg files
for file in os.listdir(filePath):
    if file.endswith(".JPG") or file.endswith(".jpg"):
        jpegVector.append(file)
    elif file.endswith(rawType):
        rawVector.append(file)
    else:
        print("Ignoring")
jpegTotal = len(jpegVector)
rawTotal = len(rawVector)
photoTotal = jpegTotal + rawTotal
total = photoTotal
i = 0

# Go through Vector and pop each index into the JPEG or RAW folder
for photoTotal in range(photoTotal, 0, -1):
    time.sleep(.01)
    if ((photoTotal - 1) - rawTotal) > -1:
        jpegAddress = (filePath + "{}".format("/") + jpegVector[((photoTotal - 1) - rawTotal)])
        shutil.move(jpegAddress, jpeg)
        i = i + 1
        update_progress(i / total)
    else:
        rawAddress = (filePath + "{}".format("/") + rawVector[photoTotal - 1])
        shutil.move(rawAddress, raw)
        i = i + 1
        update_progress(i / total)
print("\nDone!")
