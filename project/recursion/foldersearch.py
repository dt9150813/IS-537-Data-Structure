#!/usr/bin/env python3
import os
import fnmatch


IMAGE_GLOBS = {
    '*.png',
    '*.jpg',
}

def is_image(filename):
    '''
    Returns True if the given filename matches one of the IMAGE_GLOBS patterns.
    Just check the filename itself (don't inspect the file contents).
    '''
    for ext in IMAGE_GLOBS:
        if fnmatch.fnmatch(filename, ext):
            return True


def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''
    for file in os.listdir(rootpath):
        path = os.path.join(rootpath,file)
        if os.path.isdir(path):
            yield from find_images(path)
        elif is_image(path):
            yield path
