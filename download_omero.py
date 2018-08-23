""" download images from OMERO server with list of image IDs
"""

import os
import argparse
import getpass
import numpy as np
import pandas as pd
from scipy.misc import imresize
from omero.gateway import BlitzGateway


parser = argparse.ArgumentParser(description='Download from OMERO server')
 
parser.add_argument('-s', type=str, default='images',
                    help='save directory')

parser.add_argument('-i', type=str, default='imageIDs',
                    help='csv datafile with imageID column')

parser.add_argument('-x', type=int, default=256,
                    help='save image width resolution')

parser.add_argument('-y', type=int, default=256,
                    help='save image height resolution')

parser.add_argument('-c', type=int, default=255,
                    help='save resolution')

parser.add_argument('-o', type=str, default='lincs.ohsu.edu',
                    help='OMERO host')

args = parser.parse_args()


un = raw_input('enter your OMERO username for %s:' % args.o)
pw = getpass.getpass('enter your OMERO password for %s:' % args.o)


os.makedirs(args.s)

df = pd.read_csv(args.i, usecols = ['ImageID'])

conn = BlitzGateway(un, pw, host=args.o, port=4064)
conn.connect()

for imageID in df.ImageID:
    print('downloading', imageID)
    img = conn.getObject("Image", imageID)
    pixels = img.getPrimaryPixels()
    channels = []
    for i in range(img.getSizeC()):
        ch = np.array(pixels.getPlane(0,i,0), dtype='f')
        ch = ch / np.amax(ch)*args.c
        ch = imresize(ch, (args.x, args.y))
        channels.append(ch)
    plane = np.dstack(channels)
    np.save(os.path.join(args.s, str(imageID)), plane)


print('done!')
