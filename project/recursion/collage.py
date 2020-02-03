#!/usr/bin/env python3
import argparse
import os
from PIL import Image               # pip3 install pillow
from foldersearch import find_images
import math


THUMBNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200



########################
###  Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(os.path.abspath(args.searchpath)):
        imgpaths.append(filepath)
    print(imgpaths)
    if len(imgpaths) == 0:
        print('No images found')
        return
    img_rows = math.ceil(len(imgpaths)/THUMBNAILS_PER_ROW)
    # create a new, RGB image
    collage = Image.new('RGB', (THUMBNAIL_WIDTH * THUMBNAILS_PER_ROW, img_rows * THUMBNAIL_HEIGHT))

    img_column = 0
    img_row = 0
    # place the thumbnails
    for imgnum, imgpath in enumerate(imgpaths):
        print(f'=> {imgpath}')
        # open the image and convert to RGB
        img = Image.open(imgpath)
        img.convert('RGB')
        # resize to a thumnail
        img.thumbnail((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
        # paste in next position
        collage.paste(img, (img_column * THUMBNAIL_WIDTH, img_row * THUMBNAIL_HEIGHT))
        if (img_column + 1) % 4 == 0:
            img_column = 0
            img_row +=1
        else:
            img_column += 1

    # save the image
    print(f'Writing {args.collage}')
    collage.save(args.collage)

########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
