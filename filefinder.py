import os

def printAllFlashdecks(directory = 'flashdecks/'):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        #if filename == None or file_path == None:
            #continue
        print(filename)
