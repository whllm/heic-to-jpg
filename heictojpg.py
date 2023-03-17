#HEIC to JPG image format batch conversion script for Python 3. Tested on Windows 10.
#You will need to have ImageMagick installed: https://www.imagemagick.org/

import os, subprocess

working_dir = '.'
output_dir = 'output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(working_dir):
    if filename.lower().endswith(".heic"): 
        print('Converting %s...' % os.path.join(working_dir, filename))
        subprocess.run(["magick", "%s" % filename, "%s" % (os.path.join(output_dir, filename[0:-5]) + '.jpg')])
        continue