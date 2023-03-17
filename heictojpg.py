#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess

directory = '.'
sub = '.\out'

for filename in os.listdir(directory):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(directory, filename))
        subprocess.run(["magick", "%s" % filename, "%s" % (os.path.join(sub, directory) + filename[0:-5] + '.jpg')])
        continue