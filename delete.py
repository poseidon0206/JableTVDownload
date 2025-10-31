import os

def deleteMp4(folderPath):
    files = os.listdir(folderPath)
    originFile = folderPath.split(os.path.sep)[-1] + '.mp4'
    for file in files:
        if file != originFile:
            try:
                os.remove(os.path.join(folderPath, file))
            except FileNotFoundError:
                pass


def deleteM3u8(folderPath):
    files = os.listdir(folderPath)
    for file in files:
        if file.endswith('.m3u8'):
            try:
                os.remove(os.path.join(folderPath, file))
            except FileNotFoundError:
                pass
