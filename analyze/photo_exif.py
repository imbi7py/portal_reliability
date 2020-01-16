# https://steemit.com/utopian-io/@steempytutorials/extracting-exif-meta-data-from-images-with-python

import exifread
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Open image file for reading (binary mode)
path_name = os.path.join(BASE_DIR, 'analyze/01.jpg')

def process_image(filename):
    # Open image file for reading (binary mode)
    f = open(filename, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    '''
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print("Key: %s, value %s" % (tag, tags[tag]))
    '''
    # DSLR 정보와 관련 있는 key 는 Image Make, Image Model

    return tags['Image Make']

print(f"EXIF Image Make : {process_image(path_name)}")
