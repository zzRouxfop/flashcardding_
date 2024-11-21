import os

def printAllFlashdecks():
    for filename in os.listdir('flashdecks'):
        file_path = os.path.join('flashdecks', filename)
        print(filename)
