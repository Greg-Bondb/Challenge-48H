import os
from os import listdir
from os.path import isfile, join
from exiftool import ExifToolHelper

with ExifToolHelper() as exif:
    tabFile = [f for f in listdir(os.getcwd() + '/Puzzle') if isfile(join(os.getcwd() + '/Puzzle', f))]
    for nameFile in tabFile:
        for d in exif.get_metadata(os.getcwd() + '/Puzzle/' + nameFile):
            for k, v in d.items():
                if k == "PNG:Collection":
                    file = f'{v}'[0:2] + '.png'
                    old_name = os.getcwd() + '/Puzzle/' + nameFile
                    new_name = os.getcwd() + '/Puzzle/' + file
                    os.rename(old_name, new_name)