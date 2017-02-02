#!/usr/bin/env python3

import os
import subprocess
import sys

BASE_PATH = '/media/snoraid/record'
COMMAND = ' '.join([
    'run_all.py',
    '--verbose',
    '--steps_unpack',
    '--steps_arrange',
    '--steps_isp',
    # '--steps_rectify',
    # '--rectify_file %(directory)s/rectify.yml',
    '--rectify_file /home/reality7/res/config/rectify.yml',
    '--steps_render',
    '--steps_ffmpeg',
    '--data_dir %(directory)s',
    '--dest_dir %(directory)s',
    '--enable_top',
    '--enable_bottom',
    '--enable_pole_removal',
    '--enable_render_coloradjust',
    '--save_debug_images',
    '--quality 8k',
])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('''usage: %s <directory>

where <directory> is the directory name where your .bin files are
(subdirectory of "%s")
''' % (os.path.basename(sys.argv[0]), BASE_PATH))
        sys.exit(-1)

    directory = os.path.join(BASE_PATH, sys.argv[1])
    if not os.path.exists(directory):
        print('ERROR: the directory "%s" does not exist' % directory)
        sys.exit(-2)

    cmd = COMMAND % dict(directory=directory)

    print('running: %s' % cmd)
    subprocess.call(cmd, shell=True)

